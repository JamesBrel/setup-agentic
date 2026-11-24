# Skill: Application Security (`application-security`)

## 1. Purpose
Secure coding practices, OWASP Top 10 mitigation, cryptographic standards, and vulnerability remediation.

## 2. Activation Conditions
- Designing authentication and authorization subsystems
- Security code reviews and vulnerability assessments
- Remediating SAST/DAST findings and patching CVEs

## 3. Required Knowledge
- OWASP Top 10 (Injection, Broken Auth, Sensitive Data Exposure, SSRF, XSS, CSRF)
- Cryptographic best practices (Argon2id for passwords, AES-256-GCM for encryption)
- Token security: JWT signing, rotation, expiration, and revocation algorithms
- Input sanitization, output encoding, and parameterized database queries

## 4. Execution Methodology
- 1. Threat Identification: Map entry points, untrusted input boundaries, and sensitive data flows.
- 2. Input Validation: Enforce strict allow-lists and schema validation on all inputs.
- 3. Parameterization: Ensure all database interactions utilize parameterized prepared statements.
- 4. Authentication & Authorization: Enforce strong password hashing and RBAC checks on every route.
- 5. Sensitive Data Protection: Encrypt sensitive data at rest and in transit (TLS 1.3).
- 6. Security Verification: Run SAST analyzers and secret scanners to certify Gate 4.

## 5. Best Practices
- Never implement custom cryptographic algorithms; use battle-tested standard libraries.
- Never log sensitive data (passwords, payment cards, session tokens, PII).
- Apply principle of least privilege to all service accounts and database users.

## 6. Common Mistakes to Avoid
- Concatenating raw strings into SQL queries or shell execution strings.
- Hardcoding credentials or API keys into git repository code or configuration files.
- Relying solely on client-side validation without backend verification.

## 7. Validation Criteria
- Zero Critical or High severity findings in SAST and dependency scans.
- Automated secret scanning confirms zero committed secrets.
- All endpoints requiring authorization return 401/403 when unauthenticated.

## 8. Relevant Tools
`Semgrep, SonarQube, OWASP ZAP, TruffleHog, Gitleaks`

## 9. Authoritative References
- OWASP Top Ten & OWASP ASVS (Application Security Verification Standard)
- NIST SP 800-63B: Digital Identity Guidelines
