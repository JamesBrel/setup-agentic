# Skill: CI/CD Engineering (`cicd-engineering`)

## 1. Purpose
Continuous integration, automated testing workflows, and automated continuous deployment pipelines.

## 2. Activation Conditions
- Constructing GitHub Actions, GitLab CI, or Cloud Build pipelines
- Automating build, test, lint, and packaging tasks on branch pushes
- Configuring release tagging, semver generation, and artifact publishing

## 3. Required Knowledge
- Declarative CI/CD pipeline syntaxes (GitHub Actions workflow YAML)
- Pipeline caching strategies (dependency caches, Docker layer caches)
- Matrix builds across OS platforms and runtime language versions
- Deployment strategies: Blue-Green, Canary, Rolling updates

## 4. Execution Methodology
- 1. Trigger Definition: Configure workflow triggers for pull_request and push to main.
- 2. Job Parallelization: Split linting, testing, and security scanning into concurrent jobs.
- 3. Dependency Caching: Cache package manager directories (node_modules, pip cache, pub cache).
- 4. Artifact Generation: Build production binaries, containers, or web distribution bundles.
- 5. Quality Gate Enforcement: Block PR merge if any verification job fails.
- 6. Release Automation: Automatically generate release notes and publish packages on git tags.

## 5. Best Practices
- Ensure total CI pipeline execution time remains under 10 minutes for fast feedback.
- Use environment secrets and OpenID Connect (OIDC) instead of static cloud access keys.
- Pin action dependencies to commit SHAs to prevent supply chain poisoning.

## 6. Common Mistakes to Avoid
- Allowing failing test steps to continue with continue-on-error: true.
- Rebuilding Docker images or recompiling code from scratch without layer caching.
- Granting broad write permissions (GITHUB_TOKEN) when read-only is sufficient.

## 7. Validation Criteria
- actionlint passes on all workflow YAML files with zero errors.
- PR pipeline successfully runs all unit tests, linters, and gate checks.
- Build artifacts are cleanly packaged and published to registry.

## 8. Relevant Tools
`GitHub Actions, actionlint, GitLab CI, act (local GitHub Actions)`

## 9. Authoritative References
- Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation by Jez Humble & David Farley
- GitHub Actions Documentation (docs.github.com/actions)
