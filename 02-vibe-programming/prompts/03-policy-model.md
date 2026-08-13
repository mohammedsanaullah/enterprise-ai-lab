# Prompt 03 — Policy Model

## Purpose

Implement the policy data model as the first step of the application. No other application functionality should be implemented at this stage.

## Context Provided to AI

I asked Copilot to use:

- `requirements.md`
- `02-architecture-analysis.md`

## Prompt

Read the following project context before doing anything:

- requirements.md
- the architecture documented in 02-architecture-analysis.md

We are implementing the Vehicle Insurance Policy Generator incrementally.

For this step, implement ONLY the policy data model.

Create:

vehicle-insurance/src/policy.py

Requirements:

1. Create a Policy class.
2. The Policy must represent:
   - customer name
   - vehicle manufacturing year
   - vehicle price
   - yearly premium
   - policy number
   - issue date
3. Use Decimal for monetary values.
4. Use appropriate Python type hints.
5. Keep the class simple.
6. Do not implement:
   - CLI input
   - validation
   - premium calculation
   - PDF generation
   - filename handling
7. Do not create any other files.
8. Explain the design decisions before providing the code.

Follow the existing requirements and architecture. Do not invent additional business rules.

## AI Response

Copilot proposed a Python `Policy` dataclass containing:

- `customer_name: str`
- `vehicle_year: int`
- `vehicle_price: Decimal`
- `yearly_premium: Decimal`
- `policy_number: str`
- `issue_date: date`

It used:

- `@dataclass`
- `Decimal` for monetary values
- `date` for the issue date
- Python type hints


## My Review

I accepted Copilot's proposed `Policy` data model.

### Decisions I accepted

- I used `@dataclass` because the class primarily represents policy data.
- I used `Decimal` for vehicle price and yearly premium because these fields represent monetary values.
- I used `date` for the issue date rather than storing it as a string.
- I kept the model free from validation, calculation, CLI and PDF logic.

### Correction

The generated response had an indentation issue in the class docstring and fields. I corrected the formatting so that the Python code is syntactically valid.

## Final Decision

I accepted the implementation because it follows the architecture and keeps the `Policy` class focused on representing policy data.

This was my first implementation step using an AI-generated solution, which I reviewed and corrected before accepting.