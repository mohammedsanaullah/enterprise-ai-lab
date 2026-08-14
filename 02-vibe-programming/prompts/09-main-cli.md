# Prompt 09 — Main CLI 

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

## Prompt

Read the following project context before doing anything:

- requirements.md
- 02-architecture-analysis.md
- vehicle-insurance/src/policy.py
- vehicle-insurance/src/validation.py
- vehicle-insurance/src/premium_calculator.py
- vehicle-insurance/src/filename_utils.py
- vehicle-insurance/src/pdf_generator.py
- vehicle-insurance/src/policy_number.py

We are implementing the Vehicle Insurance Policy Generator incrementally.

For this step, implement ONLY the CLI orchestration.

Create:

vehicle-insurance/src/main.py

The CLI should:

1. Ask the user for:
   - customer name
   - vehicle manufacturing year
   - vehicle price

2. Validate the inputs using the existing functions in validation.py.

3. Calculate the yearly premium using premium_calculator.py.

4. Generate a policy number using policy_number.py.

5. Create a Policy object using policy.py.

6. Generate the filename using filename_utils.py.

7. Generate the PDF using pdf_generator.py.

8. Display a clear success message including the generated PDF path.

Error handling:

- Handle invalid user input gracefully.
- Display a clear error message instead of showing an unhandled traceback for expected validation errors.
- Do not silently continue after invalid input.
- Handle PDF/file-generation errors gracefully where practical.

Architecture constraints:

- main.py is orchestration only.
- Do not duplicate validation logic.
- Do not duplicate premium calculation.
- Do not generate policy numbers directly in main.py.
- Do not generate PDF content directly in main.py.
- Do not implement filename sanitisation directly in main.py.
- Use the existing modules.

Keep the CLI simple and beginner-friendly.

Do not modify the existing modules.
Do not create tests yet.
Do not create additional files.

Before providing the code, briefly explain how main.py coordinates the existing modules.

Do not invent new business rules.

## AI Response

Copilot created `main.py` as the orchestration layer.

It collects the three user inputs, delegates validation and premium
calculation to the existing modules, generates a policy number,
constructs the `Policy` object, creates a safe unique filename and
generates the PDF.

## My Review

I reviewed the orchestration and confirmed that business logic remains
in the appropriate modules rather than being duplicated in `main.py`.

I removed broad exception handling so unexpected programming errors
are not hidden during development.

I tested the CLI end-to-end and confirmed that a policy PDF was
successfully generated.

## My Decision

I accepted the implementation after reviewing the module integration
and successfully running the application.

## Learning

I learned how the individual modules developed through Vibe Programming
can be composed into a complete working application while keeping
each responsibility separate.

## Additional Human Decision

I decided that generated PDF files should be stored in a dedicated
`output/` directory rather than the project root.

This keeps generated artifacts separate from source code and makes the
project structure easier to maintain.

The output directory is created automatically if it does not exist,
and generated PDFs are excluded from Git tracking.