# Handoff - SmartBI Weekly Reporting

## What This Project Does

Defines a public-safe SmartBI reporting method without exposing internal BI routes or exports.

## How To Reuse

1. Keep all real SmartBI configs and exports in a private workspace.
2. Use `references/cli-workflow.md` to design the CLI flow.
3. Use `references/security-boundary.md` before packaging any output.
4. Build fake configs and fake outputs before publishing runnable examples.

## Extension Notes

- Add a fully fake minimal CLI demo before moving real scripts into this repository.
- Keep writeback actions behind approval, dry-run, and rollback guards.
- Never include report IDs, tenant links, cookies, or exported workbooks.
