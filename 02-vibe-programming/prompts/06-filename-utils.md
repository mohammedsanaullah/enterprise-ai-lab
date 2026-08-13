# Prompt 06 — Filename Utils 

## Purpose

Implement the policy data model as the first step of the application. No other application functionality should be implemented at this stage.

## Context Provided to AI

I asked Copilot to use:

- `requirements.md`
- `02-architecture-analysis.md`
- `03-policy-model.md`
- `04-input-validation.md`
- `05-premium-calculator.md`

## Prompt

Read the following project context before doing anything:

- requirements.md
- 02-architecture-analysis.md
- vehicle-insurance/src/policy.py
- vehicle-insurance/src/validation.py
- vehicle-insurance/src/premium_calculator.py

We are implementing the Vehicle Insurance Policy Generator
incrementally.

For this step, implement ONLY filename handling.

Create:

vehicle-insurance/src/filename_utils.py

Implement:

1. sanitize_customer_name()
2. build_policy_filename()
3. resolve_unique_filename()

Requirements:

- The final filename should follow:
  <customer-name>-policy.pdf

- Customer names may contain:
  - spaces
  - punctuation
  - special characters
  - leading or trailing whitespace

- Sanitise the customer name so the filename is safe for common
  operating systems.

- Preserve the customer's name as much as reasonably possible.
  Do not unnecessarily remove meaningful characters.

- Normalise whitespace.

- Do not allow path traversal or directory separators in the generated filename.

- If a file with the same name already exists, do not overwrite it. Generate a unique filename using a clear suffix such as: `<customer-name>-policy-1.pdf`

- Keep filename handling independent from the CLI and PDF generation.

- Do not implement PDF generation.
- Do not modify policy.py.
- Do not modify validation.py.
- Do not modify premium_calculator.py.
- Do not create tests yet.
- Do not create any other files.

Use pathlib where appropriate.

Before providing the code, briefly explain your filename sanitisation and collision-handling approach.

Do not invent unrelated functionality.

 ## AI Response

Copilot implemented three filename utilities:

- `sanitize_customer_name()` creates a safe lowercase kebab-case name.
- `build_policy_filename()` creates the `<customer-name>-policy.pdf` naming pattern.
- `resolve_unique_filename()` prevents existing files from being overwritten by adding a numeric suffix.

The implementation also handles whitespace, special characters, path separators, long names and Unicode characters.

## My Review

I accepted the overall design because filename sanitisation and collision handling are kept separate from the business logic and PDF generation.

I chose lowercase kebab-case filenames to make the generated files predictable and portable across operating systems.

I also kept the implementation dependency-free and avoided adding unnecessary complexity.

## My Decision

I accepted the implementation after reviewing the sanitisation and duplicate filename behaviour.

## Learning

I learned that filename handling is a separate responsibility from the policy logic and that user-provided names should never be used directly as filesystem paths.