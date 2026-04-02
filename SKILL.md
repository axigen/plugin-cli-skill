---
name: axigen-cli
description: Use when the user needs to manage an Axigen mail server - creating domains, accounts, configuring services, running diagnostics, or any Axigen CLI administration task
---

# Axigen CLI Skill

Manage Axigen mail servers through the telnet-based admin CLI (port 7000). This skill supports two modes:

1. **Generate commands** - produce CLI command sequences the user copy-pastes into a terminal.
2. **Execute live** - run commands against a server using the Python helper (`axigen_cli.py` in this skill directory).

For full command syntax in every context, consult `cli-reference.md` in this skill directory.

## Protocol Overview

- Transport: plain TCP to port 7000 (telnet protocol). Line endings are CRLF.
- Authentication: send `user <username>`, then the password on the next prompt.
- Response codes: `+OK` = success, `-ERR` = failure.
- The prompt indicates the current context: `<#>` (root), `<domain#>`, `<account#>`, `<account-quotas#>`, etc.

## Context Navigation Model

The CLI is a hierarchical context tree. You must navigate to the correct context before issuing commands.

```
Root (<#>)
  ├── UPDATE Domain <name>        -> domain context
  │     ├── UPDATE Account <name> -> account context
  │     │     ├── CONFIG Quotas   -> quotas subcontext
  │     │     │     └── DONE      -> back to account
  │     │     └── COMMIT          -> back to domain
  │     └── COMMIT                -> back to root
  ├── CONFIG Server               -> server context
  ├── CONFIG Imap / SmtpIncoming / SmtpOutgoing / Pop3 / etc.
  └── ADD Domain <name>           -> domain-create context
```

### Navigation Rules

1. Navigate to the correct context before issuing commands.
2. `COMMIT` saves changes in the current context and returns to the parent.
3. `BACK` discards changes and returns to the parent.
4. `DONE` saves and returns from subcontexts (quotas, limits, webmaildata, etc.).
5. `ADD` creates a new object - enters its context, set attributes, then `COMMIT`.
6. `UPDATE` enters an existing object for modification.
7. `SAVE Config` at root persists all running changes to disk.
8. For multiple independent changes, navigate back to root between each one.

## Command Generation Rules

When generating CLI command sequences for the user:

- Always navigate to the correct context first.
- Always end with `COMMIT` (not `BACK`) if changes were made.
- Always include `SAVE Config` at root after making changes.
- Use `<password>` as a placeholder for passwords - never hardcode real passwords.
- Show one command per line.
- Add `# explanation` comments for complex sequences.

## Executing Commands

There are two tools available for running CLI commands on a live server:

### Option A: `axigen_cli.py` (bundled with this skill)

Takes commands as separate arguments — suited for structured, multi-step sequences with error control:

```bash
# Execute a sequence of commands
python3 axigen_cli.py --commands 'CMD1' 'CMD2' 'CMD3'

# Single read-only query
python3 axigen_cli.py --query 'LIST Domains'

# Dump CLI help tree from the server
python3 axigen_cli.py --dump-help /tmp/cliHelp.txt
```

Use the path relative to this skill directory (where this SKILL.md lives). If the skill is installed at a known path, use that absolute path.

**Required environment variables:**

| Variable      | Required | Default  | Description              |
|---------------|----------|----------|--------------------------|
| `AXIGEN_HOST` | Yes      | -        | Server hostname or IP    |
| `AXIGEN_PORT` | No       | `7000`   | CLI port                 |
| `AXIGEN_USER` | No       | `admin`  | Admin username           |
| `AXIGEN_PASS` | Yes      | -        | Admin password           |

### Option B: `run-cli.py` (official Axigen automation script)

Download from: https://www.axigen.com/mail-server/scripts/download/?tool=run-cli.py  
Recommended install path: `/opt/axigen/scripts/run-cli.py`

Commands are passed as a **single string separated by `|`** (pipe). This script is simpler and faster to use for one-liners, shell scripts, and bulk operations.

```bash
# Basic usage — pipe commands in a single quoted string
./run-cli.py "update domain my.domain.org|list accounts"

# FOREACH — iterate over all domains or accounts (virtual command)
./run-cli.py "foreach domain|list accounts"

# FOREACH over all accounts in all domains
CLIRESPONSE=0 ./run-cli.py "foreach domain|foreach account|config contactinfo|show|back"

# Read commands from stdin (use - as the argument)
echo "list domains" | ./run-cli.py -

# SSL connection
./run-cli.py "list domains" admin-password 127.0.0.1:7000:ssl
```

**Configuration — environment variables or inline args:**

| Variable / Arg        | Description                                       |
|-----------------------|---------------------------------------------------|
| `CLIHOST`             | Server IP (default: `127.0.0.1`)                  |
| `CLIPORT`             | CLI port (default: `7000`)                        |
| `CLIPASS`             | Admin password (env var)                          |
| `CLIRESPONSE`         | Output verbosity: `1`=full (default), `0`=silent, `2`=minimal |
| 2nd positional arg    | Admin password (overrides `CLIPASS`)              |
| 3rd positional arg    | `host[:port[:conn-type]]` — `conn-type`: `raw` or `ssl` |

**Special virtual commands (only in `run-cli.py`):**

| Command          | Description                                              |
|------------------|----------------------------------------------------------|
| `FOREACH DOMAIN` | Iterates over all active domains                         |
| `FOREACH ACCOUNT`| Iterates over all accounts in current domain context     |
| `REMOVE-ITEM`    | Removes the current FOREACH item (e.g. delete account)   |
| `info`           | Prints the current object name inside a FOREACH loop     |
| `SHOW ATTR`      | Extended SHOW with attribute details                     |

**When to prefer `run-cli.py` over `axigen_cli.py`:**
- Bulk operations across all domains or accounts (`FOREACH`)
- Shell one-liners and cron jobs (simpler invocation syntax)
- The script is already installed on the Axigen server (`/opt/axigen/scripts/`)
- Piping commands from stdin or another script

**When to prefer `axigen_cli.py`:**
- Need JSON output for programmatic parsing
- Structured multi-step sequences with context-aware error handling
- Invoked by Claude to automate tasks in this skill

## Looking Up Command Syntax

When you need command syntax for a specific context, read the relevant section from `cli-reference.md` in this skill directory. **Do NOT read the entire file** - it is over 2500 lines.

Use targeted lookups:

1. Grep for the section header: `Grep for "## Context: domain$"` in `cli-reference.md`.
2. Read ~170 lines from that match offset to get the full context section.

Examples:
- Domain commands: grep for `## Context: domain$`
- Account commands: grep for `## Context: account$`
- SMTP outgoing: grep for `## Context: smtpOutgoing$`
- Queue management: grep for `## Context: queue$`

## Refreshing the CLI Reference

When the user wants to update the reference to match their server version:

1. Run `python3 axigen_cli.py --dump-help /tmp/cliHelp.txt` to extract the help tree.
2. Retrieve the dump from the server: `scp <host>:/tmp/cliHelp.txt .`
3. Convert the dump to markdown following the same format as `cli-reference.md`.
4. Replace `cli-reference.md` with the new version.

## Safety Rules

### REQUIRE user confirmation before executing

These commands are destructive or disruptive. Always ask the user to confirm before running them:

- `REMOVE` - deletes accounts, domains, listeners, etc.
- `PURGE` - permanently removes messages, metadata, or backups
- `STOP Service` - takes a service offline
- `COMPACT` - compacts storage (locks mailboxes)
- `RESET` - resets configuration to last saved state
- Any command in a `DEBUG` context

### Run freely (read-only)

These commands are safe to execute without confirmation:

- `SHOW`, `LIST`, `HELP`, `QUERY`

### Password handling

- Use `<password>` placeholder in generated command sequences.
- For live execution, read passwords from the `AXIGEN_PASS` environment variable. Never echo or log passwords.
- When creating accounts, ask the user to provide the account password.

## Common Task Recipes

### Create a domain

```
ADD Domain name example.com postmasterPassword <password>
SET domainLocation /var/opt/axigen/domains/example.com
ADD MessagesLocation file:///var/opt/axigen/domains/example.com/messages
COMMIT
SAVE Config
```

### Create an account

```
UPDATE Domain example.com
ADD Account name john password <password>
COMMIT
BACK
SAVE Config
```

### Create an account with quota

```
UPDATE Domain example.com
ADD Account name john password <password>
CONFIG Quotas
SET messageSizeQuota 1073741824
DONE
COMMIT
BACK
SAVE Config
```

### List domains

```
LIST Domains
```

### List accounts in a domain

```
UPDATE Domain example.com
LIST Accounts
BACK
```

### Change account password

```
UPDATE Domain example.com
UPDATE Account name john
SET password <password>
COMMIT
BACK
SAVE Config
```

### Start/stop a service

```
# Stop IMAP
CONFIG Imap
STOP Service
COMMIT
SAVE Config
```

```
# Start IMAP
CONFIG Imap
START Service
COMMIT
SAVE Config
```

### Configure SMTP relay

```
CONFIG SmtpOutgoing
SET relayHost relay.example.com
SET relayPort 25
COMMIT
SAVE Config
```

### Check DNS resolution

```
CONFIG Dnr
QUERY MX example.com
BACK
```

### View mail queue

```
CONFIG Queue
LIST Messages
BACK
```
