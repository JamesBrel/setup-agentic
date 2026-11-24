# Skill: Node.js & TypeScript (`nodejs-typescript`)

## 1. Purpose
Asynchronous backend microservices and API development on Node.js using TypeScript.

## 2. Activation Conditions
- Developing Node.js REST, GraphQL, or gRPC backend services
- Authoring Express, Fastify, or NestJS service modules
- Handling asynchronous streams, workers, and event loop performance

## 3. Required Knowledge
- Node.js event loop architecture (timers, poll, check, close, process.nextTick)
- Modern asynchronous JavaScript (async/await, Promise combinators, AbortController)
- Fastify and Express framework middleware pipelines and error handling
- Worker threads and child processes for CPU-intensive tasks

## 4. Execution Methodology
- 1. Project Scaffolding: Setup TypeScript compilation, tsx/ts-node, and ESLint.
- 2. Server Bootstrap: Configure Fastify/Express with security middleware (Helmet, CORS).
- 3. Route & Controller Implementation: Map REST endpoints to controller handlers.
- 4. Service & Repository Layer: Implement domain logic with dependency injection.
- 5. Error Handling: Centralize error middleware converting domain exceptions to RFC 7807.
- 6. Verification: Run tsc, eslint, and jest/vitest suites.

## 5. Best Practices
- Always use Fastify for high-throughput JSON APIs over older Express versions.
- Never execute synchronous blocking I/O (fs.readFileSync) in request handlers.
- Always register unhandledRejection and uncaughtException listeners for graceful shutdown.

## 6. Common Mistakes to Avoid
- Blocking the single-threaded event loop with expensive cryptographic or CPU loops.
- Swallowing unhandled promise rejections leading to hung HTTP requests.
- Failing to clean up event listeners causing memory leaks.

## 7. Validation Criteria
- TypeScript compiles cleanly with strict null checks enabled.
- Server demonstrates zero unhandled promise rejections under load testing.
- Integration test suite validates all endpoints.

## 8. Relevant Tools
`Node.js, TypeScript, Fastify, Jest, Vitest, Pino Logger`

## 9. Authoritative References
- Node.js Documentation (nodejs.org/docs)
- Node.js Best Practices GitHub Repository
