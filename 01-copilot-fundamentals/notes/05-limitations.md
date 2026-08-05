# Limitations

Understanding Copilot’s limitations is critical for trustworthy AI-powered architecture and development.

## Purpose

- Set realistic expectations for what Copilot can and cannot do.
- Identify where human review is mandatory.
- Avoid relying on AI for critical design judgments.

## Common Limitations

1. **Accuracy is not guaranteed**
   - Copilot can suggest incorrect logic, outdated APIs, or incomplete error handling.
   - Example: generated code may use deprecated cloud SDK methods or assume an unsupported configuration.

2. **Security and compliance risks**
   - Automatically generated code may omit secure defaults or data protection controls.
   - Example: missing input validation, hard-coded secrets, or overly broad permissions in infrastructure code.

3. **Context scope is limited**
   - Copilot may not fully understand the entire architecture from a large repository.
   - Example: it may suggest a service integration without recognizing existing orchestration patterns.

4. **Can hallucinate details**
   - The assistant may invent functions, classes, or even configuration fields that do not exist.
   - Example: suggesting a fictitious `validateTenantAccess()` helper when no such module exists.

5. **Not a replacement for architect judgment**
   - Copilot helps generate options, but the final choice should be driven by business, security, and performance requirements.
   - Example: selecting a data store still requires analysis of consistency, latency, and cost tradeoffs.

## Real-Time Use Case Examples

- Review any generated Terraform snippet for least privilege before applying it.
- Validate generated auth flows against your organization’s identity management policy.
- Use generated code as a first draft, then refine it to fit the architecture and governance model.
