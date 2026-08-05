# Refactoring Prompts

This file captures prompt examples for using Copilot to refactor code, simplify logic, and improve structure.

## Purpose

- Enable safer, faster refactoring with AI guidance.
- Improve modularity, readability, and reuse.
- Help preserve architecture intent while reducing complexity.

## Prompt Examples

1. **Simplify a complex function**
   - Prompt: "Refactor the selected code to make it simpler and easier to maintain while preserving behavior."
   - Real use case: cleaning up a monolithic data transformation function in a data pipeline.

2. **Extract reusable components**
   - Prompt: "Suggest how to extract shared logic into a reusable helper or service."
   - Real use case: turning duplicate API request handling logic into a single client wrapper.

3. **Improve naming and structure**
   - Prompt: "Refactor variable and function names to better reflect business intent and architecture."
   - Real use case: renaming generic handlers to match domain events in an event-driven design.

4. **Streamline cloud resource definitions**
   - Prompt: "Refactor this infrastructure-as-code snippet to remove duplication and make it reusable."
   - Real use case: consolidating repeated Azure resource blocks into a reusable module.
