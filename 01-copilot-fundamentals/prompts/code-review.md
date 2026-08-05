# Code Review Prompts

This file captures prompt examples for using Copilot to review code, identify issues, and suggest improvements.

## Purpose

- Help architects and engineers get a second opinion on implementation details.
- Surface potential bugs, security issues, and architecture smells.
- Improve code quality before peer review.

## Prompt Examples

1. **Review a function for correctness and style**
   - Prompt: "Review the selected code for correctness, readability, and potential edge cases. Suggest improvements and point out any security concerns."
   - Real use case: reviewing an input validation function for a payment API.

2. **Assess cloud configuration**
   - Prompt: "Check this Terraform or ARM template for security best practices, least privilege, and naming consistency."
   - Real use case: validating a new Azure Storage account definition before deployment.

3. **Find architectural issues**
   - Prompt: "Analyze this service implementation and identify any scalability or maintainability issues."
   - Real use case: reviewing an event-driven integration layer for potential bottlenecks.

4. **Extract review feedback**
   - Prompt: "Summarize the main improvements needed in this code and provide a short prioritized list."
   - Real use case: generating a concise review summary for a pull request description.
