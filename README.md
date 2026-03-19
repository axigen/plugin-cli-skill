# Axigen CLI Skill for Claude Code

Manage [Axigen](https://www.axigen.com) mail servers directly from Claude Code. Create domains, accounts, configure services, manage queues, and more — all through natural language.

## CAUTION: Use with Care in Production

> **AI-generated commands may contain errors.** The language model may hallucinate commands that don't exist, omit critical steps (such as COMMIT or SAVE CONFIG), or navigate to the wrong CLI context. Destructive commands (REMOVE, PURGE, DELETE) executed without verification can cause **permanent data loss**. Service commands (STOP Service) can cause immediate outages.
>
> **Recommendations:**
> 1. **Always review generated commands** before executing on production servers
> 2. **Test on a staging environment first** — use a [Docker instance](https://www.axigen.com/documentation/deploying-running-axigen-in-docker-p686522391) for validation
> 3. **Back up your configuration** (`SAVE CONFIG`) before making bulk changes
> 4. **Use advisory mode** for critical operations — ask Claude for the command sequence, review it, then execute manually
> 5. **Never grant unsupervised access** to production mail servers handling real user data
>
> This skill is a productivity tool, not a replacement for administrator judgment. The authors accept no liability for data loss or service disruption resulting from AI-generated commands.

## Installation

```bash
# Add the Axigen marketplace
/plugin marketplace add axigen/plugins

# Install the skill
/plugin install axigen-cli

# Activate
/reload-plugins
```

## Quick Version Check (No Credentials Needed)

You can check the server version without authentication:

```bash
python3 axigen_cli.py --host mail.example.com --get-version
# Output: 10.6.30|Linux|x86_64
```

This sends `GET VERSION` at the `<login>` prompt — a pre-authentication command available since Axigen 10.x.

## Configuration

The skill connects to an Axigen server's CLI port (default: 7000) via telnet. You need to provide connection credentials through environment variables.

### Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `AXIGEN_HOST` | **Yes** | `127.0.0.1` | Axigen server hostname or IP address |
| `AXIGEN_PORT` | No | `7000` | CLI telnet port |
| `AXIGEN_USER` | No | `admin` | Admin username |
| `AXIGEN_PASS` | **Yes** | — | Admin password |

### Setting Credentials

**Option 1: Export in your shell profile** (persistent across sessions)

Add to your `~/.zshrc`, `~/.bashrc`, or `~/.profile`:

```bash
export AXIGEN_HOST=mail.example.com
export AXIGEN_PORT=7000
export AXIGEN_USER=admin
export AXIGEN_PASS=your-admin-password
```

Then reload: `source ~/.zshrc`

**Option 2: Export in the current terminal** (current session only)

```bash
export AXIGEN_HOST=mail.example.com
export AXIGEN_PASS=your-admin-password
```

**Option 3: Use a `.env` file with direnv** (per-project, auto-loaded)

Install [direnv](https://direnv.net/), then create a `.env` file in your project:

```bash
# .env (add to .gitignore!)
export AXIGEN_HOST=mail.example.com
export AXIGEN_PORT=7000
export AXIGEN_USER=admin
export AXIGEN_PASS=your-admin-password
```

**Option 4: Use a secrets manager**

For production environments, load credentials from your secrets manager:

```bash
export AXIGEN_PASS=$(vault kv get -field=password secret/axigen/admin)
# or
export AXIGEN_PASS=$(aws secretsmanager get-secret-value --secret-id axigen-admin --query SecretString --output text)
```

### Security Notes

- **Never commit credentials** to version control. Add `.env` to your `.gitignore`.
- The `AXIGEN_PASS` variable is read by the Python helper at runtime and never logged or echoed.
- For Docker deployments, pass credentials via `docker run -e AXIGEN_PASS=...` or Docker secrets.
- The CLI connection is unencrypted by default (plain telnet). SSL/TLS is supported with `--ssl`. Use on trusted networks or via SSH tunnel:
  ```bash
  ssh -L 7000:localhost:7000 user@mail.example.com
  export AXIGEN_HOST=127.0.0.1
  ```

## Usage

Once credentials are set, just ask Claude in natural language:

### Domain Management

> "List all domains on the server"
>
> "Create a new domain called example.com"
>
> "Disable domain old.example.com"

### Account Management

> "Create an account john@example.com with password SecurePass123"
>
> "Set the quota for john@example.com to 5GB"
>
> "Suspend the account john@example.com"
>
> "List all accounts in example.com"

### Service Configuration

> "Show the current IMAP settings"
>
> "Enable TLS 1.3 on the IMAP listener"
>
> "Start the POP3 service"

### Queue Management

> "Show me the mail queue"
>
> "Delete stuck messages older than 2 days"
>
> "Force queue delivery"

### Server Information

> "Show the server license info"
>
> "What's the server version?"
>
> "Show storage statistics for example.com"

## What's Included

| File | Description |
|------|-------------|
| `SKILL.md` | Skill definition — teaches Claude the CLI navigation model, common tasks, and safety rules |
| `axigen_cli.py` | Python helper — handles telnet connection, authentication, and command execution |
| `cli-reference.md` | Complete command reference for all 126 CLI contexts (v10.6.30) |

## How It Works

1. You ask Claude to perform an Axigen management task
2. Claude reads the skill definition to understand CLI navigation and command syntax
3. Claude constructs the appropriate command sequence
4. Commands are executed via `axigen_cli.py` which connects to the server over telnet
5. Results are displayed as a CLI transcript with prompts showing context transitions

## The CLI Navigation Model

Axigen's CLI uses a hierarchical context model. You navigate into contexts, make changes, then save:

```
<login> (pre-auth)
├── GET VERSION — no credentials needed
├── USER <user> → <password> → <#> (authenticated root)
<#> (root)
├── CONFIG SERVER → <server#>
│   ├── CONFIG IMAP → <server-imap#>
│   └── CONFIG SMTP-INCOMING → <server-smtpIncoming#>
├── UPDATE Domain name example.com → <domain#>
│   ├── UPDATE Account name john → <domain-account#>
│   │   ├── CONFIG Quotas → <domain-account-quotas#>
│   │   │   └── DONE (save quotas, return to account)
│   │   └── COMMIT (save account, return to domain)
│   └── COMMIT (save domain, return to root)
└── ENTER QUEUE → <queue#>
```

**Key commands:**
- `COMMIT` — save changes and return to parent context
- `DONE` — save sub-config (quotas, limits, etc.) and return
- `BACK` — discard changes and return to parent
- `SAVE CONFIG` — persist all changes to disk

## Direct Usage (without Claude)

You can also use `axigen_cli.py` directly from the command line:

```bash
# List domains
python3 axigen_cli.py "LIST Domains"

# Create an account (multi-command sequence)
python3 axigen_cli.py \
  "UPDATE Domain name example.com" \
  "ADD Account name john password SecurePass123" \
  "COMMIT" \
  "SAVE CONFIG"

# JSON output for scripting
python3 axigen_cli.py --json "LIST Domains"

# Read commands from a file
python3 axigen_cli.py --script commands.txt

# Continue past errors
python3 axigen_cli.py --continue-on-error "CMD1" "CMD2" "CMD3"
```

## Requirements

- Python 3.10+
- Network access to the Axigen server's CLI port (default: 7000)
- Admin credentials for the Axigen server

## License

MIT
