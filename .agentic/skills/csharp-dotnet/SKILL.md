# Skill: C# and .NET (`csharp-dotnet`)

## 1. Purpose
Cross-platform enterprise .NET 8+ development, ASP.NET Core, Entity Framework Core, and xUnit.

## 2. Activation Conditions
- Building .NET 8+ Web APIs, microservices, or background worker services
- Designing Entity Framework Core DbContexts, migrations, and LINQ queries
- Authoring xUnit / FluentAssertions test suites

## 3. Required Knowledge
- C# 12 modern language features (primary constructors, collection expressions, pattern matching)
- ASP.NET Core Minimal APIs and Controller architectures
- EF Core change tracking, migrations, and compiled queries
- Asynchronous programming with async/await, Task, and CancellationToken

## 4. Execution Methodology
- 1. Solution Structure: Scaffold solution adhering to Clean Architecture project layout.
- 2. Domain & Application: Implement domain entities and MediatR / command handlers.
- 3. Infrastructure & EF Core: Configure DbContext with Fluent API configurations.
- 4. API Endpoints: Define Minimal API routes with endpoint filters and validation.
- 5. Resiliency: Configure Polly retry and circuit breaker policies for external HTTP clients.
- 6. Verification: Run dotnet build --warnaserror and dotnet test.

## 5. Best Practices
- Always pass CancellationToken down through all asynchronous I/O methods.
- Use AsNoTracking() for read-only queries in Entity Framework Core.
- Enable nullable reference types (<Nullable>enable</Nullable>) in all .csproj files.

## 6. Common Mistakes to Avoid
- Using .Result or .Wait() on Tasks causing thread-pool starvation and deadlocks.
- Executing unbounded client-side evaluation of LINQ queries.
- Ignoring CancellationToken parameters in API controllers.

## 7. Validation Criteria
- dotnet build passes with zero warnings (warnings treated as errors).
- xUnit test suite passes with 100% success rate.
- Code adheres to .editorconfig formatting standards.

## 8. Relevant Tools
`dotnet CLI, xUnit, FluentAssertions, Polly, Testcontainers-dotnet`

## 9. Authoritative References
- Microsoft .NET Documentation (learn.microsoft.com/dotnet)
- C# in Depth by Jon Skeet
