# Skill: Python Engineering (`python-engineering`)

## 1. Purpose
Production Python development, type annotations, packaging, async programming, and pytest.

## 2. Activation Conditions
- Building Python backend services, automation scripts, or data pipelines
- Developing FastAPI, Flask, or Django applications
- Authoring pytest suites and enforcing strict typing with mypy/pyright

## 3. Required Knowledge
- Python 3.10+ features (structural pattern matching, type unions, asyncio task groups)
- Static type checking with mypy / pyright and typing protocols
- Python packaging standards (pyproject.toml, poetry, uv, pip-tools)
- Pytest fixtures, parametrization, and async test plugins

## 4. Execution Methodology
- 1. Environment & Package Configuration: Setup pyproject.toml with dependencies and tool configs.
- 2. Type-Annotated Implementation: Author domain models and logic with complete type signatures.
- 3. Framework Integration: Implement FastAPI routes with Pydantic v2 schemas.
- 4. Async Execution: Manage asynchronous coroutines with proper cancellation tokens.
- 5. Test Authoring: Construct isolated pytest fixtures with monkeypatch or unittest.mock.
- 6. Quality Checks: Execute ruff check, ruff format --check, mypy, and pytest.

## 5. Best Practices
- Use Pydantic v2 for data parsing and validation at system boundaries.
- Enforce strict mypy configuration (disallow_untyped_defs = True).
- Use ruff for blazing fast linting and formatting.

## 6. Common Mistakes to Avoid
- Mutable default arguments in function signatures (def func(items=[])).
- Mixing synchronous blocking code inside asyncio event loop without run_in_executor.
- Catching bare except: instead of specific exception classes.

## 7. Validation Criteria
- mypy passes in strict mode with zero type errors.
- ruff check and ruff format report zero issues.
- pytest achieves 100% pass rate with coverage reporting.

## 8. Relevant Tools
`uv, ruff, mypy, pytest, FastAPI, Pydantic`

## 9. Authoritative References
- Fluent Python: Clear, Concise, and Effective Programming by Luciano Ramalho
- PEP 8 - Style Guide for Python Code & PEP 484 - Type Hints
