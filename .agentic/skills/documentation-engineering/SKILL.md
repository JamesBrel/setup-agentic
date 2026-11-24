# Skill: Documentation Engineering (`documentation-engineering`)

## 1. Purpose
Technical writing, API documentation, Mermaid diagramming, and markdown linting.

## 2. Activation Conditions
- Authoring READMEs, architecture summaries, and developer portals
- Generating API references from code comments and OpenAPI specifications
- Verifying internal documentation links and code examples

## 3. Required Knowledge
- Diátaxis documentation framework (Tutorials, How-To Guides, Reference, Explanation)
- GitHub Flavored Markdown (GFM) and alert syntax (> [!NOTE], > [!IMPORTANT])
- Mermaid.js diagramming syntax (flowcharts, sequence diagrams, state diagrams)
- Automated link checking and markdown linting rules

## 4. Execution Methodology
- 1. Audience Analysis: Determine developer reader personas and operational intent.
- 2. Documentation Categorization: Structure content using the Diátaxis framework.
- 3. Visual Architecture: Author Mermaid.js diagrams illustrating data flows and states.
- 4. Code Snippet Testing: Ensure every documented command and snippet is verified executable.
- 5. Link & Formatting Verification: Run markdownlint and markdown-link-check.
- 6. Synchronization: Ensure documentation matches current codebase release tag.

## 5. Best Practices
- Keep documentation as close to the code as possible (docs/ and README.md).
- Use clear, active voice and provide copyable CLI commands with expected outputs.
- Include architecture decision context alongside pure procedural guides.

## 6. Common Mistakes to Avoid
- Documenting aspirational features that have not yet been implemented.
- Letting code snippets fall out of sync with actual API changes.
- Writing wall-of-text documentation without visual diagrams or tables.

## 7. Validation Criteria
- markdownlint passes with zero formatting errors.
- Zero broken internal links or 404 image URLs.
- All documented terminal commands execute cleanly in a fresh workspace.

## 8. Relevant Tools
`markdownlint, markdown-link-check, Mermaid.js, TypeDoc / JSDoc`

## 9. Authoritative References
- Diátaxis Documentation Framework (diataxis.fr)
- Docs for Developers: An Engineer's Field Guide to Technical Writing
