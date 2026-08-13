# Prompt 04 — Input Validation

## Purpose

Implement the policy data model as the first step of the application.
No other application functionality should be implemented at this stage.

## Context Provided to AI

I asked Copilot to use:

- `requirements.md`
- `02-architecture-analysis.md`
- `03-policy-model.md`

## Prompt

Read the following project context before doing anything:

- requirements.md
- 02-architecture-analysis.md
- vehicle-insurance/src/policy.py

We are implementing the Vehicle Insurance Policy Generator
incrementally.

For this step, implement ONLY input validation.

Create:

vehicle-insurance/src/validation.py

Implement functions for:

1. validate_customer_name()
2. validate_vehicle_year()
3. validate_vehicle_price()

Requirements:

- Customer name must not be empty or whitespace-only.
- Vehicle year must be numeric.
- Vehicle year must not be in the future.
- Vehicle year must be a reasonable manufacturing year.
- Vehicle price must be numeric.
- Vehicle price must be greater than zero.
- Vehicle price must use Decimal rather than float.
- Validation functions should return clean, typed values or raise
  clear validation errors.
- Keep validation logic independent from the CLI.
- Do not implement premium calculation.
- Do not implement PDF generation.
- Do not modify policy.py.
- Do not create tests yet.
- Do not create any other files.

Use type hints and keep the implementation simple.

Before providing the code, briefly explain the validation design
and any assumptions you made.

## AI Response

Copilot proposed three independent validation functions:

- `validate_customer_name()` cleans and validates the customer name.
- `validate_vehicle_year()` converts and validates the manufacturing year.
- `validate_vehicle_price()` converts the value to `Decimal` and rejects
  zero, negative and invalid amounts.

The implementation also rejects floats for monetary values to avoid
floating-point precision issues.

## My Review

I accepted the overall validation design because it keeps validation
separate from the CLI and business logic.

I changed the `customer_name` type hint to allow `None`, because the
function explicitly handles missing input.

I also kept the validation rules simple rather than adding unnecessary
business logic.

## My Decision

I accepted the implementation after reviewing and making the small
type-hint correction.

## Learning

I learned that AI-generated code still needs to be checked for
consistency between type hints, validation behaviour and project
requirements.