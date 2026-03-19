# Day 2: Student Record Validator

## What You're Building
A data validation tool that checks a batch of student records for errors. Instead of crashing on the first bad record, it processes ALL records and generates an error report.

## What You'll Learn
- Raising exceptions with `raise`
- Custom exception classes
- Multiple `except` blocks
- Exception chaining (`raise ... from ...`)
- Collecting errors vs. crashing on first error

## Requirements
Build `validator.py` that:

1. **Defines custom exceptions:**
   - `InvalidNameError` — name is empty or contains numbers
   - `InvalidGradeError` — grade not in valid range (0-100)
   - `InvalidEmailError` — email doesn't contain @ and .
   - `MissingFieldError` — required field is missing

2. **Validates student records** — Each record is a dictionary:
   ```python
   {"name": "Alice", "grade": 95, "email": "alice@school.edu"}
   ```

3. **Processes a batch of records** — Don't stop at the first error. Validate ALL records and collect ALL errors.

4. **Generates an error report:**
   ```
   === Validation Report ===
   Total records: 10
   Valid: 7
   Invalid: 3

   Errors:
   - Record 3 (Bob): InvalidGradeError - Grade 150 is out of range (0-100)
   - Record 5 (???): MissingFieldError - Missing required field: name
   - Record 8 (Charlie): InvalidEmailError - "charlie" is not a valid email
   ```

## How to Work
- Start by defining your custom exception classes
- Build one validator function at a time (validate_name, validate_grade, validate_email)
- Then build the batch processor that uses all validators

## Stretch Goals
- Add a `--fix` mode that attempts to auto-correct common issues (strip whitespace, capitalize names)
- Read records from a JSON file instead of hardcoded data
- Export the error report to a CSV file

## When You're Done
```
git add .
git commit -m "Day 2: Student Record Validator with custom exceptions"
git push
```
