# Prompt 07 — PDF Generator  

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

## Prompt

Read the following project context before doing anything:

- requirements.md
- 02-architecture-analysis.md
- vehicle-insurance/src/policy.py
- vehicle-insurance/src/validation.py
- vehicle-insurance/src/premium_calculator.py
- vehicle-insurance/src/filename_utils.py

We are implementing the Vehicle Insurance Policy Generator incrementally.

For this step, implement ONLY PDF generation.

Create:

vehicle-insurance/src/pdf_generator.py

Use a suitable Python PDF library. Prefer a simple, lightweight solution appropriate for a beginner learning project.

Implement:

generate_policy_pdf(policy: Policy, filename: str | Path) -> Path

The generated document must:

- contain exactly one page;
- have a professional vehicle-insurance-policy-summary appearance;
- clearly identify the document as a fictional sample;
- prominently state that it is NOT a real insurance certificate;
- contain these dynamic fields:
  - customer name
  - vehicle manufacturing year
  - vehicle value
  - yearly premium
  - policy number
  - issue date;
- contain static sample policy wording;
- clearly separate the dynamic policy details from the static wording;
- display monetary values with two decimal places;
- create the output PDF at the supplied filename.

The document should be suitable for demonstration in an Enterprise AI Engineering portfolio.

Important constraints:

- Do not calculate the premium in this module.
- Do not validate user input in this module.
- Do not generate policy numbers in this module.
- Do not modify Policy.
- Do not modify validation.py.
- Do not modify premium_calculator.py.
- Do not modify filename_utils.py.
- Do not create the CLI yet.
- Do not create tests yet.
- Do not create additional files.

The PDF must not contain language that could reasonably make it appear to be a genuine insurance certificate.

Before providing the code, briefly explain:
1. which PDF library you selected and why;
2. how the one-page layout is structured;
3. how the fictional-document disclaimer is made prominent.

Do not invent additional business rules.

## AI Response

Copilot selected ReportLab for PDF generation and created a single-page policy summary.

The layout contains:

- policy title;
- prominent fictional-document disclaimer;
- dynamic policy details;
- static sample policy wording;
- footer disclaimer.

The PDF receives a populated `Policy` object rather than raw user input or calculation logic.

## My Review

I accepted ReportLab because it is appropriate for a simple, dependency-light PDF generation task.

I accepted the separation between PDF rendering and business logic. The PDF generator does not validate inputs or calculate premiums.

I also checked that monetary values are displayed to two decimal places and that the fictional disclaimer is prominent.

## My Decision

I accepted the implementation after reviewing the layout, responsibilities and disclaimer.

## Learning

I learned how an existing data model can be passed into a presentation layer without duplicating business logic.