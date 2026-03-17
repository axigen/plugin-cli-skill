#!/usr/bin/env python3
"""
Axigen CLI helper — execute commands against an Axigen mail server via telnet.

Usage:
    python axigen_cli.py --host HOST --port PORT --user USER --pass PASS "cmd1" "cmd2" ...
    python axigen_cli.py --host HOST --port PORT --user USER --pass PASS --script commands.txt

Environment variables (fallback):
    AXIGEN_HOST, AXIGEN_PORT, AXIGEN_USER, AXIGEN_PASS

Examples:
    # List domains
    python axigen_cli.py --host mail.example.com "LIST Domains"

    # Create account
    python axigen_cli.py --host mail.example.com \
        "UPDATE Domain name example.com" \
        "ADD Account name john password SecurePass123" \
        "CONFIG ContactInfo" \
        "SET firstName John" \
        "SET lastName Doe" \
        "DONE" \
        "COMMIT"

    # Interactive: read commands from stdin (one per line)
    echo -e "LIST Domains\\nEXIT" | python axigen_cli.py --host mail.example.com --stdin
"""

import argparse
import json
import os
import re
import socket
import sys
import time


class AxigenCLIError(Exception):
    """Raised when a CLI command returns -ERR."""
    pass


class AxigenCLI:
    """Stateful telnet client for the Axigen CLI."""

    def __init__(self, host: str, port: int = 7000, timeout: float = 10.0):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = None
        self.current_prompt = ""
        self.banner = ""

    def connect(self) -> str:
        """Connect to the Axigen CLI. Returns the welcome banner."""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(self.timeout)
        self.sock.connect((self.host, self.port))
        self.banner = self._read_response()
        # Extract prompt
        self.current_prompt = self._extract_prompt(self.banner)
        return self.banner

    def login(self, user: str, password: str) -> str:
        """Authenticate with the CLI. Returns the response."""
        resp = self.send(f"USER {user}")
        resp += self.send(password)
        if "-ERR" in resp:
            raise AxigenCLIError(f"Authentication failed: {resp.strip()}")
        return resp

    def send(self, command: str) -> str:
        """Send a command and return the full response including prompt."""
        if self.sock is None:
            raise AxigenCLIError("Not connected")
        self.sock.sendall((command + "\r\n").encode())
        resp = self._read_response()
        self.current_prompt = self._extract_prompt(resp)
        return resp

    def execute(self, command: str) -> dict:
        """Execute a command and return structured result.

        Returns:
            {
                "command": "the command sent",
                "prompt_before": "<domain#>",
                "prompt_after": "<domain-account#>",
                "response": "full response text",
                "success": True/False,
                "error": "error message if any"
            }
        """
        prompt_before = self.current_prompt
        resp = self.send(command)

        # Check for error
        success = "-ERR" not in resp
        error = ""
        if not success:
            # Extract error message
            for line in resp.split("\n"):
                if "-ERR" in line:
                    error = line.strip()
                    break

        return {
            "command": command,
            "prompt_before": f"<{prompt_before}>",
            "prompt_after": f"<{self.current_prompt}>",
            "response": resp.strip(),
            "success": success,
            "error": error,
        }

    def close(self):
        """Close the connection."""
        if self.sock:
            try:
                self.sock.sendall(b"EXIT\r\n")
                time.sleep(0.3)
            except Exception:
                pass
            try:
                self.sock.close()
            except Exception:
                pass
            self.sock = None

    def _read_response(self) -> str:
        """Read until we see a prompt pattern."""
        data = b""
        deadline = time.time() + self.timeout
        while time.time() < deadline:
            try:
                chunk = self.sock.recv(8192)
                if not chunk:
                    break
                data += chunk
                text = data.decode("utf-8", errors="replace")
                # Check for prompt patterns: <login>, <password>, <#>, <context#>
                if re.search(r'<[^>]*>\s*$', text.rstrip()):
                    return text
                # Check for connection close
                if '+OK: have a nice day' in text:
                    return text
            except socket.timeout:
                break
        return data.decode("utf-8", errors="replace")

    @staticmethod
    def _extract_prompt(text: str) -> str:
        """Extract the prompt name from response text."""
        m = re.search(r'<([^>]*)>\s*$', text.rstrip())
        return m.group(1) if m else ""


def format_transcript(results: list[dict], include_banner: str = "") -> str:
    """Format execution results as a CLI transcript."""
    lines = []
    if include_banner:
        for line in include_banner.strip().split("\n"):
            lines.append(line.rstrip())

    for r in results:
        # Show prompt + command
        lines.append(f"{r['prompt_before']} {r['command']}")
        # Show response (skip the prompt at the end)
        resp_lines = r["response"].split("\n")
        for line in resp_lines:
            line = line.rstrip()
            # Skip the final prompt line (already shown in next iteration)
            if re.match(r'^<[^>]*>\s*$', line.strip()):
                continue
            if line.strip():
                lines.append(line)

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Execute commands on an Axigen CLI server",
        epilog="Commands are executed sequentially. Stops on first error unless --continue-on-error is set.",
    )
    parser.add_argument("commands", nargs="*", help="CLI commands to execute")
    parser.add_argument("--host", default=os.environ.get("AXIGEN_HOST", "127.0.0.1"),
                        help="Axigen server hostname (default: $AXIGEN_HOST or 127.0.0.1)")
    parser.add_argument("--port", type=int, default=int(os.environ.get("AXIGEN_PORT", "7000")),
                        help="CLI port (default: $AXIGEN_PORT or 7000)")
    parser.add_argument("--user", default=os.environ.get("AXIGEN_USER", "admin"),
                        help="Admin username (default: $AXIGEN_USER or admin)")
    parser.add_argument("--password", "--pass", dest="password",
                        default=os.environ.get("AXIGEN_PASS", ""),
                        help="Admin password (default: $AXIGEN_PASS)")
    parser.add_argument("--script", type=str, help="Read commands from file (one per line)")
    parser.add_argument("--stdin", action="store_true", help="Read commands from stdin")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    parser.add_argument("--transcript", action="store_true", default=True,
                        help="Output as CLI transcript (default)")
    parser.add_argument("--continue-on-error", action="store_true",
                        help="Continue executing after errors")
    parser.add_argument("--timeout", type=float, default=10.0,
                        help="Socket timeout in seconds (default: 10)")

    args = parser.parse_args()

    # Collect commands
    commands = list(args.commands)
    if args.script:
        with open(args.script) as f:
            commands.extend(line.strip() for line in f if line.strip() and not line.startswith("#"))
    if args.stdin:
        commands.extend(line.strip() for line in sys.stdin if line.strip() and not line.startswith("#"))

    if not commands:
        parser.print_help()
        sys.exit(1)

    if not args.password:
        print("Error: password required. Use --pass or set AXIGEN_PASS environment variable.", file=sys.stderr)
        sys.exit(1)

    # Connect and authenticate
    cli = AxigenCLI(args.host, args.port, args.timeout)
    try:
        banner = cli.connect()
        cli.login(args.user, args.password)
    except (ConnectionRefusedError, socket.timeout, AxigenCLIError) as e:
        print(f"Connection failed: {e}", file=sys.stderr)
        sys.exit(1)

    # Execute commands
    results = []
    exit_code = 0
    for command in commands:
        result = cli.execute(command)
        results.append(result)
        if not result["success"]:
            exit_code = 1
            if not args.continue_on_error:
                break

    cli.close()

    # Output
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print(format_transcript(results, include_banner=banner))

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
