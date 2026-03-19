# Day 5: Test Suite

## What You're Building
A comprehensive test suite for your Day 1 (Grade Calculator) and Day 3 (Weather CLI) projects. Then you'll practice TDD (Test-Driven Development) by writing a test FIRST and building a feature to make it pass.

## What You'll Learn
- `pytest` — Python's testing framework
- `assert` statements — checking expected values
- Test functions — naming conventions, structure
- Fixtures — reusable test setup
- Mocking — faking API calls for testing
- TDD — write the test first, then the code

## Setup
```
pip install pytest pytest-mock
```

## Requirements

### Part 1: Test the Grade Calculator (Day 1)
Create `test_grade_calculator.py` with tests for:
1. `calculate_gpa(["A", "B", "C"])` returns 3.0
2. `calculate_gpa(["A", "A", "A"])` returns 4.0
3. `calculate_gpa([])` handles empty list (raises error or returns 0)
4. `get_grade_input()` handles lowercase input
5. `get_grade_input()` rejects invalid grades

### Part 2: Test the Weather CLI (Day 3)
Create `test_weather.py` with tests for:
1. `display_weather()` formats data correctly
2. `fetch_weather()` handles city not found (mock the API)
3. `fetch_weather()` handles network errors (mock the API)
4. `get_api_key()` raises error when key is missing

### Part 3: TDD Challenge
Write a test FIRST for a new feature, then build it:
1. Write `test_grade_calculator.py::test_plus_minus_grades` — test that A+ = 4.0, A- = 3.7, B+ = 3.3, etc.
2. Run the test (it should FAIL)
3. Now go add +/- support to your grade calculator
4. Run the test again (it should PASS)

## How to Run Tests
```
pytest                           # Run all tests
pytest test_grade_calculator.py  # Run specific file
pytest -v                        # Verbose output
pytest -x                        # Stop on first failure
```

## How to Work
- Start with the simplest tests (happy path)
- Then add edge case tests
- Then do the TDD challenge

## Stretch Goals
- Aim for 90%+ code coverage: `pip install pytest-cov && pytest --cov`
- Add parametrized tests: `@pytest.mark.parametrize`
- Write tests for the Dice Game (Day 4) — how do you test randomness?

## When You're Done
```
git add .
git commit -m "Day 5: Test suite with pytest, mocking, and TDD"
git push
```
