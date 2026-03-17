---
name: axigen-cli
description: Use when the user needs to manage an Axigen mail server - creating domains, accounts, configuring services, running diagnostics, or any Axigen CLI task. Provides complete command reference and a Python helper for executing CLI commands via telnet.
---

# Axigen CLI Skill

You can manage Axigen mail servers through the CLI (Command Line Interface) accessible via telnet on port 7000.

## Setup

Before running commands, you need connection details. Ask the user for:
- **Host**: Axigen server hostname or IP
- **Port**: CLI port (default: 7000)
- **Admin password**: required for authentication

Set them as environment variables so subsequent calls don't need to repeat them:

```bash
export AXIGEN_HOST=mail.example.com
export AXIGEN_PORT=7000
export AXIGEN_USER=admin
export AXIGEN_PASS=thepassword
```

## Executing Commands

Use the `axigen_cli.py` helper script (located alongside this skill file) to execute CLI commands:

```bash
python /path/to/skill/axigen_cli.py "COMMAND1" "COMMAND2" "COMMAND3"
```

The script connects, authenticates, executes commands sequentially, and returns a transcript showing prompts and responses.

### Examples

**List domains:**
```bash
python axigen_cli.py "LIST Domains"
```

**Create a domain:**
```bash
python axigen_cli.py \
    "CREATE Domain name example.com domainLocation /axigen/var/domains/example.com wmFilterTemplatePath none postmasterPassword SecurePass123" \
    "COMMIT"
```

**Create an account:**
```bash
python axigen_cli.py \
    "UPDATE Domain name example.com" \
    "ADD Account name john password SecurePass123" \
    "CONFIG ContactInfo" \
    "SET firstName John" \
    "SET lastName Doe" \
    "DONE" \
    "CONFIG Quotas" \
    "SET totalMessageSize 102400" \
    "DONE" \
    "COMMIT"
```

**Delete an account:**
```bash
python axigen_cli.py \
    "UPDATE Domain name example.com" \
    "REMOVE Account name john" \
    "COMMIT"
```

**Suspend an account (set empty services via account class):**
```bash
python axigen_cli.py \
    "UPDATE Domain name example.com" \
    "UPDATE Account name john" \
    "SET mustChangePass yes" \
    "COMMIT"
```

**Configure IMAP SSL:**
```bash
python axigen_cli.py \
    "CONFIG SERVER" \
    "CONFIG IMAP" \
    "UPDATE Listener address 0.0.0.0:993" \
    "CONFIG sslControl" \
    "SET certFile /path/to/cert.pem" \
    "SET allowedVersions (tls1_2 tls1_3)" \
    "DONE" \
    "COMMIT" \
    "BACK" \
    "BACK" \
    "SAVE CONFIG"
```

**Check mail queue:**
```bash
python axigen_cli.py \
    "ENTER QUEUE" \
    "LIST" \
    "BACK"
```

**JSON output (for programmatic parsing):**
```bash
python axigen_cli.py --json "LIST Domains"
```

## CLI Navigation Model

The Axigen CLI uses a **hierarchical context model**. You navigate into contexts, make changes, then save:

### Entering Contexts
| Pattern | Example | Meaning |
|---------|---------|---------|
| `CONFIG <name>` | `CONFIG IMAP` | Enter service sub-config |
| `UPDATE <entity> name <n>` | `UPDATE Domain name example.com` | Enter entity for editing (full access) |
| `ADD <entity> [params]` | `ADD Account name john password Pass123` | Create entity and enter it |
| `CREATE <entity> [params]` | `CREATE Domain name ...` | Create top-level entity |
| `ENTER <name>` | `ENTER QUEUE` | Enter special context |

### Saving & Exiting
| Command | When to Use |
|---------|-------------|
| `COMMIT` | Save changes to an entity (domain, account, listener) and return to parent |
| `DONE` | Save sub-config changes (quotas, limits, contactInfo, sslControl) and return |
| `BACK` | **Discard** all changes and return to parent |
| `SAVE CONFIG` | Save running config to disk (from root `<#>` context) |
| `EXIT` | Close the CLI session |

### Important Rules
1. **Always COMMIT** after ADD/UPDATE operations on entities, or changes are lost
2. **Use DONE** (not COMMIT) for sub-configurations like Quotas, Limits, ContactInfo
3. **BACK discards** — it cancels all uncommitted changes in the current context
4. **SAVE CONFIG** after all changes to persist across server restarts

## Context Hierarchy

```
<#> (root)
├── CONFIG SERVER
│   ├── CONFIG IMAP / POP3 / SMTP-INCOMING / SMTP-OUTGOING / WEBMAIL / WEBADMIN / ...
│   │   ├── CONFIG AccessControl
│   │   ├── ADD/UPDATE Listener
│   │   │   └── CONFIG sslControl
│   │   └── START/STOP Service
│   ├── CONFIG FILTERS
│   │   ├── ADD ScriptFilter / SocketFilter / IntegratedFilter
│   │   └── ADD ActiveFilter
│   ├── CONFIG CLUSTER / CERTS / MOBILITY / SECURITY / USERDB / ...
│   └── CONFIG PERMISSIONS
├── UPDATE Domain name <domain>
│   ├── ADD/UPDATE Account name <account>
│   │   ├── CONFIG ContactInfo / Quotas / Limits / WebmailData / Filters / SendRecvRestrictions
│   │   └── COMMIT
│   ├── ADD/UPDATE Group / List / FolderRcpt / accountClass
│   ├── CONFIG FILTERS / adminLimits / PERMISSIONS / PUBLIC-FOLDER / MIGRATIONDATA
│   └── COMMIT
├── ENTER QUEUE
│   ├── LIST / LIST FILTER / LIST ID <id>
│   ├── DELETE <id> / DELIVER <id>
│   └── ENTER QUARANTINE
├── ENTER AACL
│   ├── ADD/UPDATE admin-group / admin-user
│   └── GRANT/REVOKE permission
└── SAVE CONFIG / SHOW LicenseInfo / SEARCH Object
```

## Common Tasks Reference

### Domain Operations
- `LIST Domains` — list all active domains
- `LIST AllDomains` — list all domains including disabled
- `CREATE Domain name <n> domainLocation <path> wmFilterTemplatePath none postmasterPassword <p>` — create domain
- `UPDATE Domain name <n>` — enter domain for full management
- `EDIT Domain name <n>` — enter domain for property changes only
- `DISABLE Domain name <n>` — deactivate a domain
- `ENABLE Domain name <n>` — reactivate a domain
- `DELETE Domain name <n>` — permanently delete a domain

### Account Operations (inside domain context)
- `LIST Accounts` — list accounts
- `ADD Account name <n> password <p>` — create account (enters account context)
- `UPDATE Account name <n>` — edit account (enters account context)
- `REMOVE Account name <n>` — delete account
- `SHOW Account name <n>` — view account details

### Account Sub-Contexts (inside account context)
- `CONFIG ContactInfo` → SET firstName, lastName, company, phone, email, etc. → `DONE`
- `CONFIG Quotas` → SET totalMessageSize, totalMessageCount, mboxCount → `DONE`
- `CONFIG Limits` → SET enableActiveSync, enableSharing, minimumPasswordLength, etc. → `DONE`
- `CONFIG WebmailData` → SET language, timeZone, skin, dateFormat → `DONE`
- `CONFIG SendRecvRestrictions` → SET enableSendRestrictions, sendPolicy → `DONE`
- `CONFIG Filters` → ADD ScriptFilter, ADD ActiveFilter → `DONE`

### Queue Operations
- `ENTER QUEUE` → `LIST` — view queued messages
- `LIST FILTER sender=<addr>` — filter by sender
- `LIST FILTER age>1d` — filter by age
- `LIST ID <id>` — view message details
- `DELETE <id>` — remove message from queue
- `FORCE QUEUE` — retry delivery of all queued messages

### Server Information
- `SHOW LicenseInfo` — license details
- `SHOW PremiumAddonsStatistics` — addon usage
- `SHOW MigrationStatus` — migration status
- `SHOW AccountingStatistics` — accounting stats
- `SEARCH Object <email>` — find account by email address
- `SAVE supportInfo` — generate diagnostics zip

## Full Command Reference

For the complete list of all commands in all 126 CLI contexts, see `cli-reference.md` in this skill directory.
