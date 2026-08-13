# Prompt 02 — Architecture Analysis

## Purpose

Use the approved requirements to propose a simple modular architecture before implementation.

## Context Provided to AI

The AI was given:

- requirements.md
- approved premium calculation rules
- project scope
- CLI requirement
- one-page PDF requirement

## Prompt

Read requirements.md carefully.

Do not write any code.

Act as a senior software architect and propose a simple architecture for this Vehicle Insurance Policy Generator.

Explain:

1. Recommended Python modules/classes
2. Responsibility of each module
3. Data flow from CLI input to PDF generation
4. Where premium calculation should live
5. Where input validation should live
6. Where filename sanitisation should live
7. How policy numbers should be generated
8. How the PDF generator should receive data

Keep the design simple and appropriate for a learning project.

Do not over-engineer it.
Do not introduce databases, web frameworks or cloud services.


## AI Response

Recommended architecture

For a learning project, keep the design simple and modular. A good structure is:

- `src/main.py`
- `src/policy.py`
- `src/validation.py`
- `src/premium_calculator.py`
- `src/filename_utils.py`
- `src/pdf_generator.py`

This keeps the CLI separate from business rules, input rules, filename handling, and PDF output.

1. Recommended Python modules/classes

- `main.py`
  - class: none required, just orchestration functions
  - responsibility: CLI input/output and flow control

- `policy.py`
  - class: `Policy`
  - responsibility: hold policy data and derived fields such as issue date, premium, policy number, and display values

- `validation.py`
  - functions: `validate_customer_name()`, `validate_vehicle_year()`, `validate_vehicle_price()`
  - responsibility: enforce the input rules and return clean typed values or validation errors

- `premium_calculator.py`
  - functions: `calculate_vehicle_age()`, `calculate_base_premium()`, `calculate_final_premium()`
  - responsibility: implement the premium business rules exactly as defined

- `filename_utils.py`
  - functions: `sanitize_customer_name()`, `build_policy_filename()`, `resolve_unique_filename()`
  - responsibility: create safe filesystem names and avoid overwriting existing files

- `pdf_generator.py`
  - class or function: `generate_policy_pdf(policy, filename)`
  - responsibility: render the one-page PDF using the policy data and write it to disk

2. Responsibility of each module

- `main.py`
  - Collects the three required inputs from the user
  - Calls validation functions
  - Calls premium calculation
  - Creates a `Policy` instance
  - Resolves the output filename
  - Invokes the PDF generator
  - Displays success / error messages

- `policy.py`
  - Defines the policy data model
  - Stores customer name, vehicle year, vehicle price, premium, policy number, issue date, and any formatted values
  - Can provide a simple factory or constructor that accepts validated inputs and assembled derived values

- `validation.py`
  - Encapsulates user input rules so they are not scattered through the CLI
  - Ensures empty, whitespace-only, non-numeric, future-year, and negative-price cases are handled consistently
  - Produces clear validation messages for the CLI

- `premium_calculator.py`
  - Keeps the premium business rules isolated
  - Makes it easy to test premium formulas separately
  - Avoids putting calculation logic inside the CLI or the PDF generator

- `filename_utils.py`
  - Keeps filename concerns separate from the domain model
  - Handles sanitization and collision avoidance
  - Ensures the generated filename is safe across operating systems

- `pdf_generator.py`
  - Is responsible only for turning a policy data object into a PDF file
  - Does not validate input or calculate premiums
  - Can be tested independently with sample policy objects

3. Data flow from CLI input to PDF generation

- User runs the app
- `main.py` prompts for customer name, vehicle year, and vehicle price
- `main.py` passes raw input into `validation.py`
- `validation.py` returns validated and converted values (e.g. string, `int`, `float`)
- `main.py` passes validated values into `premium_calculator.py`
- `premium_calculator.py` computes age, base premium, adjustment, and final premium
- `main.py` uses the validated input plus computed premium to construct a `Policy` object
- `main.py` calls `filename_utils.py` to generate a safe filename, checking for collisions
- `main.py` calls `pdf_generator.py` with the `Policy` object and the resolved filename
- `pdf_generator.py` writes the one-page PDF containing static wording plus the policy’s dynamic fields
- `main.py` reports the output location to the user

4. Where premium calculation should live

The premium calculation should live in a dedicated module such as `premium_calculator.py`. This is the core business rule logic, and isolating it makes the application easier to understand and test. It should implement:

- base premium = 3% of vehicle value
- vehicle age calculation
- age adjustment rules
- final premium rounding to two decimals

5. Where input validation should live

Input validation should live in `validation.py`. The CLI should only orchestrate gathering values and reacting to validation results. That module should encapsulate:

- empty / whitespace-only name checks
- numeric parsing for year and price
- sensible year range checks
- positive price checks

6. Where filename sanitisation should live

Filename sanitisation should live in `filename_utils.py`. It should be exactly the module responsible for:

- converting customer name to a safe slug
- removing or replacing unsafe characters
- normalizing whitespace and case
- building the `<customer-name>-policy.pdf` pattern
- avoiding unintentional overwrites by adding a suffix if needed

7. How policy numbers should be generated

Policy number generation should be a small helper in either `policy.py` or a dedicated `policy_number.py` utility. It should produce the required format:

- `VP-YYYY-XXXXXX`

Use the issue year from the current date and a simple unique six-character identifier. For a learning project, a random alphanumeric suffix or timestamp-derived string is appropriate, as long as it is deterministic enough for a single run and simple to understand.

8. How the PDF generator should receive data

The PDF generator should receive a populated `Policy` object and a target filename. That keeps the PDF layer independent of raw input and calculation details. The `Policy` object should already contain:

- customer name
- vehicle manufacturing year
- vehicle value
- yearly premium
- policy number
- issue date
- any formatted strings needed for display

The PDF generator then uses those fields plus static disclaimer text to create the one-page document.

This architecture is simple, modular, and aligned with the requirements, while avoiding unnecessary complexity for a beginner learning project.


## Human Review

### Accepted

- `main.py` for orchestration
- `policy.py` for policy data
- `validation.py` for validation
- `premium_calculator.py` for business rules
- `filename_utils.py` for filename handling
- `pdf_generator.py` for PDF generation

### Modified

#### Money representation

Copilot suggested numeric values such as `float`.

Decision:

Use Python `Decimal` for vehicle prices and premium calculations
because these values represent monetary amounts.

#### Policy number

No separate `policy_number.py` module will be created.

Policy number generation will remain within the policy domain because the project is intentionally small.

### Final Architecture

```text
vehicle-insurance/
├── README.md
├── src/
│   ├── main.py
│   ├── policy.py
│   ├── validation.py
│   ├── premium_calculator.py
│   ├── filename_utils.py
│   └── pdf_generator.py
└── tests/
```

## Learning

AI proposed the initial architecture, but I reviewed and modified it based on simplicity, maintainability, and appropriate handling of monetary values.

The final architecture reflects my engineering decisions informed by AI, rather than blindly accepting an AI-generated solution.