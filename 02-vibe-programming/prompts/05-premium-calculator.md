# Prompt 05 — Premium Calculator

## Purpose

Implement the policy data model as the first step of the application. No other application functionality should be implemented at this stage.

## Context Provided to AI

I asked Copilot to use:

- `requirements.md`
- `02-architecture-analysis.md`
- `03-policy-model.md`
- `04-input-validation.md`

## Prompt

Read the following project context before doing anything:

- requirements.md
- 02-architecture-analysis.md
- vehicle-insurance/src/policy.py
- vehicle-insurance/src/validation.py

We are implementing the Vehicle Insurance Policy Generator incrementally.

For this step, implement ONLY the premium calculation logic.

Create:

vehicle-insurance/src/premium_calculator.py

The implementation must follow the business rules already defined in requirements.md.

Rules:

1. Calculate vehicle age as:
   current year - vehicle manufacturing year

2. Calculate the base premium as:
   3% of the vehicle price

3. Apply the following vehicle-age adjustments:

   0–3 years  → 0%
   4–7 years  → 10%
   8+ years   → 20%

4. Calculate the final premium as:
   base premium × (1 + age adjustment)

5. Return the final premium rounded to two decimal places.

6. Use Decimal for all monetary calculations.
7. Do not use float for monetary calculations.
8. Keep the calculation logic independent from the CLI.
9. Do not implement PDF generation.
10. Do not modify policy.py.
11. Do not modify validation.py.
12. Do not create tests yet.
13. Do not create any other files.

Before providing the code, explain briefly how you interpreted the premium calculation rules.

Do not invent or change any business rules.

## AI Response

Copilot implemented the premium calculation according to the business rules in `requirements.md`.

The implementation:

- calculates vehicle age from the manufacturing year;
- calculates the base premium at 3% of vehicle value;
- applies the 0%, 10% or 20% age adjustment;
- calculates the final premium using `Decimal`;
- rounds the result to two decimal places using `ROUND_HALF_UP`.

Copilot also made `current_year` optional so the calculation can be tested using a fixed year.

## My Review

I accepted the calculation because it matches the business rules I defined in `requirements.md`.

I specifically retained the use of `Decimal` for monetary calculations and the optional `current_year` because it makes the calculation deterministic and easier to test.

I also kept validation outside this module so that the premium calculator remains focused on business logic.

## My Decision

I accepted the implementation after reviewing the calculation logic against the agreed premium rules.

## Learning

I learned that business rules should be isolated from input handling and that making time-dependent calculations testable is an important design consideration.