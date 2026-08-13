#!/usr/bin/env bash

set -e

echo "======================================"
echo "      CI/CD Dashboard - Local CI"
echo "======================================"

cd "$(dirname "$0")/../backend"

echo ""
echo "======================================"
echo "1. CODE FORMAT CHECK - BLACK"
echo "======================================"

black --check app tests

echo ""
echo "======================================"
echo "2. LINTING - RUFF"
echo "======================================"

ruff check app tests

echo ""
echo "======================================"
echo "3. LINTING - FLAKE8"
echo "======================================"

flake8 app tests

echo ""
echo "======================================"
echo "4. TESTS"
echo "======================================"

pytest -v

echo ""
echo "======================================"
echo "5. COVERAGE QUALITY GATE"
echo "======================================"

pytest \
    --cov=app \
    --cov-report=term-missing \
    --cov-fail-under=80

echo ""
echo "======================================"
echo "6. SECURITY - BANDIT"
echo "======================================"

bandit -r app

echo ""
echo "======================================"
echo "7. DEPENDENCY SECURITY - PIP-AUDIT"
echo "======================================"

pip-audit

echo ""
echo "======================================"
echo "        LOCAL CI PASSED"
echo "======================================"
