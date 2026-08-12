# Vehicle Insurance Policy Generator — Requirements

## 1. Project Purpose

Build a fictional Vehicle Insurance Policy Generator as a learning project
for the Enterprise AI Lab.

The application will demonstrate Vibe Programming by using AI assistance
for requirements analysis, architecture, implementation, testing and review.

The application will accept basic vehicle and customer information,
calculate a yearly insurance premium, and generate a one-page PDF policy
document.

The generated document is strictly a fictional learning artifact and must
clearly state that it is not a real insurance certificate.

---

## 2. User Interface

The application will initially use a Command Line Interface (CLI).

The user will provide:

- Customer name
- Vehicle manufacturing year
- Vehicle price

The application will generate one insurance policy per execution.

---

## 3. Functional Requirements

### 3.1 Customer Information

The application must accept a customer name.

The customer name:

- must not be empty;
- must be suitable for display in the PDF;
- must be sanitised when used as part of the output filename.

### 3.2 Vehicle Information

The application must accept:

- Vehicle manufacturing year
- Vehicle price

The manufacturing year must represent a reasonable past or current year.

The vehicle price must be a positive monetary value.

### 3.3 Premium Calculation

The yearly premium will be calculated using the following business rules.

#### Base Premium

Base premium = 3% of vehicle value.

#### Vehicle Age Adjustment

Vehicle age is calculated as:

Vehicle age = Current year - Vehicle manufacturing year

| Vehicle Age | Adjustment |
|---|---:|
| 0–3 years | 0% |
| 4–7 years | +10% |
| 8+ years | +20% |

The final yearly premium is:

Final premium = Base premium + Age adjustment

The premium must be rounded to two decimal places.

### 3.4 Policy Number

Each generated policy must have a policy number using this format:

`VP-YYYY-XXXXXX`

Where:

- `YYYY` is the policy issue year.
- `XXXXXX` is a unique six-character identifier.

### 3.5 Issue Date

The policy must contain the date on which the policy document is generated.

The date should use a clear human-readable format.

### 3.6 PDF Generation

The application must generate a one-page PDF policy document.

The PDF must contain:

- Customer name
- Vehicle manufacturing year
- Vehicle value
- Yearly premium
- Policy number
- Issue date
- Static policy information
- Fictional/sample disclaimer

The document should have a professional policy-summary appearance while
remaining clearly identifiable as a fictional learning artifact.

### 3.7 Output Filename

The generated PDF must follow this naming convention:

`<customer-name>-policy.pdf`

The customer name must be sanitised so that the generated filename is safe
for the operating system.

If a file with the same name already exists, the application must avoid
unintentionally overwriting the existing policy.

A suitable numeric suffix may be added, for example:

`mohammed-sanaullah-policy.pdf`

`mohammed-sanaullah-policy-2.pdf`

---

## 4. Fictional Document Disclaimer

The generated PDF must clearly state that it is a fictional sample.

The document must not appear to be an authentic insurance certificate.

The disclaimer should communicate that:

> This document is a fictional sample generated for educational and
> demonstration purposes and is not a valid insurance certificate or
> evidence of insurance coverage.

---

## 5. Input Validation

The application must handle invalid input gracefully.

### Customer Name

Reject:

- empty input;
- whitespace-only input.

The name should be sanitised before being used in the filename.

### Vehicle Year

Reject:

- empty input;
- non-numeric input;
- unreasonable years;
- future manufacturing years.

### Vehicle Price

Reject:

- empty input;
- non-numeric input;
- zero;
- negative values.

The application should provide a useful error message and allow the user
to correct invalid input.

---

## 6. Edge Cases

The application should consider:

- empty customer name;
- whitespace-only customer name;
- special characters in customer name;
- customer names containing characters unsafe for filenames;
- future vehicle year;
- extremely old vehicle year;
- invalid vehicle year;
- zero vehicle price;
- negative vehicle price;
- extremely high vehicle price;
- duplicate output filenames;
- inability to write the PDF;
- unexpected PDF generation errors.

---

## 7. Non-Functional Requirements

The application should be:

- simple;
- modular;
- readable;
- maintainable;
- testable;
- suitable for a Python learning project;
- suitable for demonstrating AI-assisted software development.

The application should not introduce unnecessary infrastructure.

The initial implementation will not use:

- databases;
- web frameworks;
- cloud services;
- external APIs;
- authentication systems.

---

## 8. Expected Data Flow

The expected application flow is:

CLI input
→ Input validation
→ Vehicle age calculation
→ Premium calculation
→ Policy data creation
→ Filename generation
→ PDF generation
→ Save PDF
→ Display output location

---

## 9. Scope

### In Scope

- Python CLI application
- Customer input
- Vehicle input
- Input validation
- Premium calculation
- Policy number generation
- Issue date generation
- Filename sanitisation
- One-page PDF generation
- Basic automated tests
- AI-assisted development and code review

### Out of Scope

- Real insurance integration
- Real insurance providers
- Real policy issuance
- Payment processing
- Customer database
- Authentication
- Claims processing
- Web interface
- Cloud deployment
- Email delivery
- Legal insurance terms

---

## 10. Definition of Done

The project will be considered complete when:

- [ ] A user can run the CLI application.
- [ ] The user can enter a customer name.
- [ ] The user can enter a vehicle manufacturing year.
- [ ] The user can enter a vehicle price.
- [ ] Invalid inputs are handled gracefully.
- [ ] The yearly premium is calculated according to the defined rules.
- [ ] A policy number is generated.
- [ ] An issue date is generated.
- [ ] A one-page PDF is created.
- [ ] The PDF contains the required dynamic fields.
- [ ] The PDF contains static policy information.
- [ ] The PDF clearly identifies itself as a fictional sample.
- [ ] The filename follows the required naming convention.
- [ ] Existing files are not unintentionally overwritten.
- [ ] Automated tests cover the main business rules and validation.
- [ ] The implementation has been reviewed by the developer.
- [ ] The project documentation explains how AI was used during development.