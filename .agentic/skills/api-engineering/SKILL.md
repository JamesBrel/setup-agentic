# Skill: API Engineering (`api-engineering`)

## 1. Purpose
Design, standardization, versioning, and documentation of RESTful, GraphQL, and gRPC APIs.

## 2. Activation Conditions
- Designing client-server or service-to-service interfaces
- Authoring OpenAPI (Swagger) specifications
- Standardizing error payloads and pagination models

## 3. Required Knowledge
- HTTP semantics, status codes (200, 201, 204, 400, 401, 403, 404, 409, 422, 500)
- REST resource modeling, idempotency (GET, PUT, DELETE), and caching headers
- RFC 7807 Problem Details for standardized error payloads
- OpenAPI 3.0 / 3.1 schema specification and contract testing

## 4. Execution Methodology
- 1. Resource Modeling: Identify nouns, hierarchies, and sub-resources (e.g. /users/{id}/orders).
- 2. Method Binding: Assign appropriate HTTP verbs respecting idempotency.
- 3. OpenAPI Authoring: Draft complete OpenAPI spec including request/response schemas.
- 4. Standardization: Enforce standard pagination (cursor or limit/offset) and RFC 7807 error format.
- 5. Authentication & Security: Define Bearer JWT auth, CORS policies, and rate limits.
- 6. Contract Verification: Validate OpenAPI document with Spectral linter and contract tests.

## 5. Best Practices
- Always version APIs via URL (/v1/) or Accept header to maintain backward compatibility.
- Provide consistent snake_case or camelCase JSON naming conventions across all endpoints.
- Validate incoming request payloads strictly against schema before executing business logic.

## 6. Common Mistakes to Avoid
- Returning 200 OK with an error payload inside the response body.
- Using verbs in URL paths (/getUser, /createOrder) instead of HTTP methods.
- Exposing internal database IDs or stack traces in error responses.

## 7. Validation Criteria
- OpenAPI specification passes Spectral validation with 0 errors.
- All endpoints return RFC 7807 compliant error structures on invalid input.
- Automated contract tests pass against actual endpoint responses.

## 8. Relevant Tools
`Spectral, Swagger UI, Postman / Newman, Prism Mock Server`

## 9. Authoritative References
- RESTful Web APIs by Leonard Richardson & Mike Amundsen
- RFC 7807: Problem Details for HTTP APIs (IETF)
