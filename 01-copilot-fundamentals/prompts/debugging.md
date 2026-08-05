# Debugging Prompts

This file captures prompt examples for using Copilot to diagnose and resolve issues in code and architecture.

## Purpose

- Accelerate root cause analysis.
- Surface likely bugs and runtime issues quickly.
- Provide guidance for remediation and testing.

## Prompt Examples

1. **Identify runtime errors**
   - Prompt: "Inspect the selected code and identify any runtime errors, exceptions, or misconfigurations."
   - Real use case: debugging a failing cloud function that processes incoming events.

2. **Check for race conditions**
   - Prompt: "Analyze this concurrent code and identify any race conditions, deadlocks, or ordering issues."
   - Real use case: validating a distributed lock implementation in a microservice workflow.

3. **Validate error handling**
   - Prompt: "Review the error handling logic and suggest better ways to handle retries and failures."
   - Real use case: improving retry logic for an external API call from a backend service.

4. **Diagnose configuration problems**
   - Prompt: "Look at this configuration file and tell me if anything looks incorrect or incompatible with the target environment."
   - Real use case: checking a Kubernetes manifest or deployment pipeline YAML for missing fields.
