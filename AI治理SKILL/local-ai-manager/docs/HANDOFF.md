# Handoff - Local AI Manager

## What This Project Does

Defines a local-first method for checking AI workspace health, Codex context size, skill directories, automations, and basic security hygiene.

## How To Reuse

1. Start with read-only scans.
2. Report only paths, sizes, risk types, and suggested actions.
3. Do not print raw session content, environment values, or secrets.
4. Use reversible archive manifests for context cleanup.

## Extension Notes

- Add a minimal public-safe CLI before committing any scanner code.
- Keep local reports and raw session data out of Git.
- Treat deletion and archival as user-confirmed actions only.
