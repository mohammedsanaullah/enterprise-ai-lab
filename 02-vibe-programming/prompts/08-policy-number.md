# Prompt 08 — Policy Number 

## Purpose

Implement the policy data model as the first step of the application. No other application functionality should be implemented at this stage.

## Context Provided to AI

I asked Copilot to use:

- `requirements.md`
- `02-architecture-analysis.md`
- `03-policy-model.md`
- `04-input-validation.md`
- `05-premium-calculator.md`
- `06-filename-utils.md`
- `07-pdf-generator.md`

## Prompt

Read the following project context before doing anything:

- requirements.md
- 02-architecture-analysis.md
- vehicle-insurance/src/policy.py
- vehicle-insurance/src/validation.py
- vehicle-insurance/src/premium_calculator.py
- vehicle-insurance/src/filename_utils.py
- vehicle-insurance/src/pdf_generator.py

We are implementing the Vehicle Insurance Policy Generator incrementally.

For this step, implement ONLY policy number generation.

Create:

vehicle-insurance/src/policy_number.py

Implement:

generate_policy_number()

The policy number must follow this format:

VP-YYYY-XXXXXX

Where:

- VP identifies the fictional Vehicle Policy.
- YYYY is the issue year.
- XXXXXX is a six-character uppercase alphanumeric identifier.

Requirements:

- Use the current date to determine the issue year by default.
- Allow the issue year to be supplied optionally so the function is
  deterministic and testable.
- Generate a new identifier for each call.
- Use only uppercase letters and digits for the six-character suffix.
- Keep the implementation simple.
- Do not use external dependencies.
- Do not modify Policy.
- Do not modify validation.py.
- Do not modify premium_calculator.py.
- Do not modify filename_utils.py.
- Do not modify pdf_generator.py.
- Do not create the CLI yet.
- Do not create tests yet.
- Do not create any other files.

Before providing the code, briefly explain how the policy number is generated and how you made it testable.

Do not invent additional business rules.

## AI Response

Copilot implemented `generate_policy_number()` using the required `VP-YYYY-XXXXXX` format.

It uses the current year by default and accepts an optional issue year for testing. The six-character suffix is generated using uppercase letters and digits.

## My Review

I accepted the implementation because it follows the agreed policy number format and keeps policy number generation separate from the Policy data model.

I corrected the description of `issue_year` so it is clear that it controls the year for testing, while the identifier remains randomly generated.

## My Decision

I accepted the implementation after reviewing the format and generation approach.

## Learning

I learned that generated identifiers should have a clear format and
that time-dependent values can be made easier to test by allowing
controlled inputs.