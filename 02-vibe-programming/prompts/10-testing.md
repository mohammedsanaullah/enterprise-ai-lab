# Prompt 10 — Automated Testing 

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
- `08-policy-number.md`
- `09-main-cli.md`

## Prompt

Read the project requirements, architecture notes and all existing source files before writing tests.

We now have a working Vehicle Insurance Policy Generator.

For this step, create automated tests for the existing application.

Focus on behaviour and business rules, not implementation details.

Test at least:

1. Customer name validation
   - valid name
   - empty name
   - whitespace-only name

2. Vehicle year validation
   - valid current/past year
   - non-numeric input
   - future year
   - year before 1886

3. Vehicle price validation
   - valid positive price
   - zero
   - negative value
   - invalid numeric input

4. Premium calculation
   - vehicle age 0–3
   - vehicle age 4–7
   - vehicle age 8+
   - two-decimal rounding
   - Decimal arithmetic

5. Policy number
   - correct VP-YYYY-XXXXXX format
   - correct issue year
   - six-character uppercase alphanumeric suffix

6. Filename handling
   - normal customer name
   - spaces
   - special characters
   - duplicate filename handling

7. PDF generation
   - PDF file is created
   - output path is correct
   - generated PDF contains exactly one page

Use pytest.

Create tests in:

vehicle-insurance/tests/

Keep tests separate from production code.

Do not modify the existing source modules unless a genuine defect is discovered.

Before providing the tests, briefly explain the test strategy.

Do not create tests for functionality that does not exist.

## AI Response

AI proposed a pytest-based test strategy derived from the agreed requirements. The tests cover input validation, premium calculation, policy number format, filename sanitisation and collision handling, PDF generation, required PDF content, and the fictional disclaimer.

The tests focus on observable behaviour rather than implementation details and use temporary files and deterministic test data where appropriate.

## Human Review

I reviewed the AI-generated tests against the agreed requirements.

I changed the PDF page-count test because the original approach inspected PDF internals rather than testing the observable requirement.

I also corrected the filename collision test. The original test expected a second filename without first creating the first generated file.

The final tests focus on expected behaviour rather than implementation details.

## Learning

This was my first automated testing step in the project. I learned that a test creates a known situation, runs the application behaviour, and uses assertions to check whether the result matches the requirement.

I also learned that AI-generated tests still require human review.