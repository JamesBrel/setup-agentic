# Skill: React & TypeScript (`react-typescript`)

## 1. Purpose
Web client application development using React 18+, TypeScript, functional components, and hooks.

## 2. Activation Conditions
- Building interactive web UI applications and SPAs/SSGs
- Developing custom React hooks and reusable component libraries
- State management with Zustand, Redux Toolkit, or React Query

## 3. Required Knowledge
- TypeScript strict mode (generics, mapped types, discriminated unions)
- React fiber reconciliation, hooks lifecycle (useState, useEffect, useMemo, useCallback)
- Server components vs Client components (Next.js App Router)
- State management libraries (TanStack Query, Zustand, Context)

## 4. Execution Methodology
- 1. Project Configuration: Setup tsconfig.json with strict: true and path aliases.
- 2. Component Design: Author typed functional components with explicit Props interfaces.
- 3. Hook Engineering: Encapsulate stateful logic and data fetching in custom hooks.
- 4. Data Management: Implement React Query for server cache and Zustand for client state.
- 5. Styling & Tokens: Apply Tailwind CSS or CSS Modules referencing design tokens.
- 6. Verification: Run tsc --noEmit, eslint ., and vitest run.

## 5. Best Practices
- Never use any; use unknown with type guards or discriminated unions.
- Keep useEffect focused on synchronization with external systems, not derived state.
- Memoize callbacks and expensive computations passed down to memoized child components.

## 6. Common Mistakes to Avoid
- Missing dependencies in useEffect dependency arrays causing stale closures.
- Mutating state directly instead of creating immutable updates.
- Prop drilling through many component levels instead of using composition or store.

## 7. Validation Criteria
- tsc --noEmit passes with zero TypeScript diagnostic errors.
- ESLint passes with zero warnings or errors.
- Unit tests achieve > 80% branch coverage with React Testing Library.

## 8. Relevant Tools
`TypeScript, Vite, ESLint, Vitest, React Testing Library`

## 9. Authoritative References
- React Official Documentation (react.dev)
- TypeScript Handbook (typescriptlang.org)
