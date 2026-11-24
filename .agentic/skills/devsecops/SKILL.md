# Skill: DevSecOps (`devsecops`)

## 1. Purpose
Integrating automated security scanning, policy-as-code, and compliance gates into DevOps lifecycles.

## 2. Activation Conditions
- Configuring CI/CD security scanning stages
- Container vulnerability scanning and base image hardening
- Enforcing branch protection rules and signed commits

## 3. Required Knowledge
- Security shifting left: SAST, DAST, SCA (Software Composition Analysis), and Secret Scanning
- Container security: Minimal distroless base images, non-root users, vulnerability scanners (Trivy)
- Policy as Code (Open Policy Agent, Conftest, Kyverno)
- Supply chain security: SBOM generation (CycloneDX, SPDX) and artifact signing (Cosign)

## 4. Execution Methodology
- 1. Pipeline Integration: Embed SCA (npm audit, pip-audit) and SAST into pull request triggers.
- 2. Secret Detection: Add pre-commit and CI secret scanning hooks (Gitleaks).
- 3. Container Hardening: Author Dockerfiles using unprivileged users and distroless/alpine bases.
- 4. Container Scanning: Execute Trivy vulnerability scans on built images in CI.
- 5. SBOM Generation: Export Software Bill of Materials for release artifacts.
- 6. Quality Gate Enforcer: Configure automated build failure on any High or Critical CVE.

## 5. Best Practices
- Fail CI builds immediately upon detecting newly introduced High/Critical vulnerabilities.
- Pin all CI third-party actions to full commit SHA hashes instead of mutable tags.
- Run containers with read-only root filesystems whenever feasible.

## 6. Common Mistakes to Avoid
- Running containers as the default root user inside production clusters.
- Allowing developers to bypass CI security gates without signed executive exemption.
- Failing to scan transitive dependencies in lockfiles.

## 7. Validation Criteria
- CI pipeline executes SAST, SCA, and secret scanning on every pull request.
- Container image scan reports zero unpatched Critical vulnerabilities.
- SBOM artifact generated and attached to release bundle.

## 8. Relevant Tools
`Trivy, Snyk, Gitleaks, Cosign, Open Policy Agent`

## 9. Authoritative References
- NIST Special Publication 800-204: Security Strategies for Microservices
- CIS Benchmarks for Docker and Kubernetes
