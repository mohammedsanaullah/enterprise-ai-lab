# Architecture Prompts

This file captures prompt examples for using Copilot to explore architecture decisions, design patterns, and system tradeoffs.

## Purpose

- Help architects quickly evaluate options and tradeoffs.
- Capture design patterns and justification in writing.
- Support communication with stakeholders and engineering teams.

## Prompt Examples

1. **Explore system design options**
   - Prompt: "Compare a serverless event-driven design versus a container-based API for this use case. List pros and cons for scalability, cost, and operational complexity."
   - Real use case: deciding between Azure Functions and AKS for a new ingestion service.

2. **Review integration patterns**
   - Prompt: "Suggest the best integration pattern for connecting this upstream system to downstream data consumers."
   - Real use case: selecting between pub/sub, batch load, or direct API calls for system integration.

3. **Assess security architecture**
   - Prompt: "Evaluate this architecture for identity, access control, and data protection risks."
   - Real use case: reviewing a multi-tenant SaaS design for authentication and segmentation gaps.

4. **Document decision rationale**
   - Prompt: "Write a concise architecture decision record for choosing this pattern, including key constraints and expected benefits."
   - Real use case: creating a reusable ADR for why an event mesh was chosen in a distributed system.
