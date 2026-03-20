# Day 2: Student Record Validator
# Validate a batch of student records and generate an error report.


# --- Custom Exceptions ---

class InvalidNameError(Exception):
    """Raised when a student name is invalid."""
    pass


class InvalidGradeError(Exception):
    """Raised when a grade is out of range."""
    pass


class InvalidEmailError(Exception):
    """Raised when an email format is invalid."""
    pass


class MissingFieldError(Exception):
    """Raised when a required field is missing."""
    pass


# --- Validators ---

def validate_name(name):
    """Validate that name is non-empty and contains only letters/spaces."""
    if name == "" or name == None:
        raise InvalidNameError("Name cannot be empty")

    for _ in name:
        if _ == " ":
            continue
        if not _.isalpha():
            raise InvalidNameError("Name must contain only letters")


def validate_grade(grade):
    """Validate that grade is a number between 0 and 100."""
    if not isinstance(grade, (int, float)):
        raise InvalidGradeError("Grade must be a number.")

    if grade < 0 or grade > 100:
        raise InvalidGradeError("Grade must be between 0 and 100.")


def validate_email(email):
    """Validate basic email format (contains @ and .)."""
    if not ("@" in email and "." in email):
        raise InvalidEmailError("Invalid email address")


def validate_record(record):
    """Validate a single student record. Returns list of errors."""
    errors = []

    # Step 1: check for missing fields
    for field in ["name", "grade", "email"]:
        if field not in record:
            errors.append(f"Missing required field: {field}")

    # Step 2: validate the fields that exist
    if "name" in record:
        try:
            validate_name(record["name"])
        except InvalidNameError as e:
            errors.append(str(e))

    if "email" in record:
        try:
            validate_email(record["email"])
        except InvalidEmailError as e:
            errors.append(str(e))

    if "grade" in record:
        try:
            validate_grade(record["grade"])
        except InvalidGradeError as e:
            errors.append(str(e))

    return errors


def validate_batch(records):
    """Validate all records and generate a report."""
    valid = 0
    invalid = 0
    all_errors = []

    for record in records:
        errors = validate_record(record)
        if len(errors) == 0:
            valid += 1
        else:
            invalid += 1
            all_errors.extend(errors)

    print("=== Validation Report ===")
    print(f"Total records: {valid + invalid}")
    print(f"Valid: {valid}")
    print(f"Invalid: {invalid}")

    print("\nErrors:")
    for _ in all_errors:
        print(f"- {_}")


# --- Sample Data ---

SAMPLE_RECORDS = [
    {"name": "Alice Johnson", "grade": 95, "email": "alice@school.edu"},
    {"name": "Bob Smith", "grade": 87, "email": "bob@school.edu"},
    {"name": "", "grade": 72, "email": "nobody@school.edu"},
    {"name": "Charlie123", "grade": 88, "email": "charlie@school.edu"},
    {"name": "Diana Prince", "grade": 150, "email": "diana@school.edu"},
    {"name": "Eve Wilson", "grade": 91, "email": "eve-no-domain"},
    {"grade": 85, "email": "missing@school.edu"},
    {"name": "Frank Lee", "grade": -5, "email": "frank@school.edu"},
    {"name": "Grace Kim", "grade": 96, "email": "grace@school.edu"},
    {"name": "Hank Brown", "grade": 78, "email": "hank@school.edu"},
]


if __name__ == "__main__":
    validate_batch(SAMPLE_RECORDS)
