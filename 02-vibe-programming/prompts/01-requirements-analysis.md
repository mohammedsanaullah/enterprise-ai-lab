# Prompt 01 — Requirements Analysis

## Purpose

Analyse the initial business idea and identify the requirements before
writing any code.

## Prompt

I am building a learning project for an Enterprise AI Engineering
portfolio.

The project is a fictional Vehicle Insurance Policy Generator.

A user should provide:
- customer name
- vehicle manufacturing year
- vehicle price

The application should calculate a yearly insurance premium and
generate a one-page PDF policy document named:

<customer-name>-policy.pdf

The PDF should contain mostly static policy information with a
small number of dynamic fields such as customer name, vehicle
year, vehicle value, yearly premium, policy number and issue date.

This is a fictional learning application and must clearly state
that the generated document is a sample and not a real insurance
certificate.

Before writing any code:

1. Analyse the business requirements.
2. Identify functional requirements.
3. Identify non-functional requirements.
4. Identify input validation requirements.
5. Identify potential edge cases.
6. Identify business rules that need to be decided.
7. Suggest questions that a developer should clarify before
   implementation.

Do not generate code.
Do not assume missing business rules.



## AI Response

### Business requirements

The application is a learning-focused Vehicle Insurance Policy Generator that:
- accepts customer information and vehicle details,
- calculates a yearly insurance premium,
- generates a one-page PDF policy document,
- names the PDF `<customer-name>-policy.pdf`,
- clearly labels the output as a fictional sample, not a real insurance certificate.

## Functional requirements

- Collect user inputs:
  - customer name
  - vehicle manufacturing year
  - vehicle price
- Compute a yearly insurance premium from the provided vehicle data.
- Generate a one-page PDF policy document.
- Populate the PDF with:
  - customer name
  - vehicle year
  - vehicle value
  - yearly premium
  - policy number
  - issue date
  - static policy wording and the sample disclaimer
- Save the PDF using the naming convention: `<customer-name>-policy.pdf`.
- Ensure the generated document explicitly states it is a sample and not a real insurance certificate.

## Non-functional requirements

- The PDF should be readable and formatted as a single page.
- The document should look like a policy summary, with static text plus dynamic values.
- The sample disclaimer must be obvious and unambiguous.
- The application should be suitable for a beginner enterprise AI engineering portfolio: simple, modular, and maintainable.
- Generated files should be correctly named and safe for filesystem use.
- The system should handle invalid input gracefully rather than crashing.

## Input validation requirements

- `customer name`
  - must not be empty
  - should contain valid characters for display
  - may need sanitization for filename generation
- `vehicle manufacturing year`
  - must be numeric
  - should be within a reasonable range (e.g., not in the far future)
  - should likely be a past or current year
- `vehicle price`
  - must be numeric
  - must be positive
  - should probably be greater than zero
- General validation
  - detect missing fields
  - reject invalid formats
  - avoid generating malformed filenames from customer names

## Potential edge cases

- Empty or whitespace-only customer name
- Names with special characters that are invalid in filenames
- Vehicle year in the future
- Vehicle year far in the past
- Non-numeric or malformed year input
- Zero or negative vehicle price
- Extremely high vehicle price
- Duplicate customer names causing filename collisions
- Missing or partial input
- Failure to write the PDF file due to filesystem permissions
- Policy number generation collision or invalid formatting
- Unexpected PDF library errors

## Business rules that need to be decided

- Premium calculation formula:
  - percentage of vehicle value?
  - age-based adjustment?
  - fixed base rate plus value multiplier?
- Interpretation of `vehicle manufacturing year`
  - model year vs actual production year
- Premium rounding rules:
  - round to whole currency units?
  - allow cents?
- Policy number format
  - sequential, random, or structured string?
- Issue date formatting
  - ISO, local date, human-readable
- Filename rules
  - how to sanitize customer name
  - whether to overwrite existing files or append a suffix
- Static policy content
  - what legal-like text is included
  - the exact wording of the disclaimer
- Scope of the document
  - only one page, no additional attachments or metadata

## Questions to clarify before implementation

- What exact formula should be used to calculate the yearly premium?
- Should the year be restricted to a specific range, and how should future years be handled?
- What is the required format for `customer-name` in the PDF filename?
- Should the application overwrite an existing PDF for the same customer name or create a unique file?
- What should the policy number look like?
- What exact disclaimer wording is required to make it clear the document is fictional?
- Is there any preferred layout or styling for the one-page PDF?
- Should the application support multiple inputs in one run or only one policy per execution?
- Where should the PDF be saved by default?
- Is there a user interface expectation (CLI, web form, desktop app)?


## Human Review

### Accepted

- CLI-based application
- One-page PDF
- Dynamic customer and vehicle information
- Filename based on customer name
- Fictional-document disclaimer
- Input validation

### Decisions made by me

- Premium calculation will use a 3% base rate.
- Vehicle age will affect the premium.
- Premium will use two decimal places.
- The application will generate one policy per execution.
- The application will remain a CLI application.

### Rejected / Changed

Copilot suggested several business rules that had not yet been
defined. These were not automatically accepted.

The premium formula was explicitly decided by myself rather
than delegated to AI.

## Learning

This exercise demonstrated that Vibe Programming should begin with
requirements analysis rather than immediately generating code.

I used AI to identify requirements and raise important questions, while I retained responsibility for the final business decisions.