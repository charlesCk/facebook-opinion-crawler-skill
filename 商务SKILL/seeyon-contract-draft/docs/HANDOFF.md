# Handoff - Seeyon Contract Draft

## What This Project Does

Creates a Seeyon OA contract application draft from runtime-provided contract files and user credentials, then verifies persisted form values before reporting success.

## How To Reuse

1. Copy `references/config.example.json` to a private path outside Git.
2. Add OA URL, runtime account, contract file path, and required field overrides.
3. Run:

```bash
node 商务SKILL/seeyon-contract-draft/scripts/create_seeyon_contract_draft.mjs /tmp/seeyon-contract-config.json
```

4. Review the draft URL and verification snapshot.
5. Submit manually only after human review.

## Extension Notes

- Add field selectors conservatively and prefer visible labels.
- Keep all real credentials and contract files outside the repository.
- If OA form fields change, update `references/field-checklist.md` and smoke checks.
