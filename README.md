# Лабораторная работа: CI с GitHub Actions

Вариант 5: Python + ruff + pytest-cov + poetry build.

## Этапы CI
1. Lint — проверка кода через ruff.
2. Test — запуск тестов через pytest-cov.
3. Build — сборка проекта через poetry build.

## Запуск
poetry install --no-interaction
poetry run ruff check .
poetry run pytest
poetry build
