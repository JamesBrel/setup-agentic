# Skill: Laravel & PHP (`laravel-php`)

## 1. Purpose
Modern enterprise PHP development using the Laravel framework, Eloquent ORM, and Artisan tooling.

## 2. Activation Conditions
- Building Laravel backend web applications and REST APIs
- Authoring Eloquent models, migrations, and database seeders
- Implementing queue workers, scheduled tasks, and event listeners

## 3. Required Knowledge
- PHP 8.2+ modern features (enums, readonly classes, fibers, attributes)
- Laravel service container, service providers, and dependency injection
- Eloquent ORM, eager loading, query scopes, and relationships
- Laravel testing tools (PHPUnit, Pest, database migrations, HTTP assertions)

## 4. Execution Methodology
- 1. Domain / Feature Scaffolding: Create migrations, models, controllers, and Form Requests.
- 2. Business Logic Implementation: Implement domain actions or use cases outside controllers.
- 3. Eloquent Relations: Define relationships with explicit foreign keys and eager loading.
- 4. Validation & Authorization: Author Form Requests and Policies for access control.
- 5. Asynchronous Work: Dispatch queue jobs with backoff and timeout parameters.
- 6. Verification: Run php artisan test --parallel and phpstan analyse --level=8.

## 5. Best Practices
- Keep controllers skinny; delegate business logic to dedicated Action classes or Services.
- Always prevent N+1 queries by eager loading relationships with with().
- Use strict types declaration (declare(strict_types=1);) in every PHP file.

## 6. Common Mistakes to Avoid
- Executing database queries directly inside Blade templates or API resource transformations.
- Failing to protect mass assignment with $fillable or strict casting.
- Disabling CSRF or authentication middleware without documented rationale.

## 7. Validation Criteria
- php artisan test passes with zero failures.
- PHPStan analysis passes at level 8 with zero errors.
- Zero N+1 query warnings detected in test profiling.

## 8. Relevant Tools
`PHPStan, Pest PHP, PHP_CodeSniffer, Laravel Pint, Artisan`

## 9. Authoritative References
- Official Laravel Documentation (laravel.com/docs)
- PHP Standards Recommendations (PHP-FIG PSR-1, PSR-4, PSR-12)
