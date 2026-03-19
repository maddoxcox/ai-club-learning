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
    # TODO: Check if name is empty or None
    # TODO: Check if name contains numbers
    # TODO: Raise InvalidNameError with descriptive message
    pass


def validate_grade(grade):
    """Validate that grade is a number between 0 and 100."""
    # TODO: Check type
    # TODO: Check range
    # TODO: Raise InvalidGradeError
    pass


def validate_email(email):
    """Validate basic email format (contains @ and .)."""
    # TODO: Check for @ and .
    # TODO: Raise InvalidEmailError
    pass


def validate_record(record):
    """Validate a single student record. Returns list of errors."""
    errors = []
    # TODO: Check for required fields (name, grade, email)
    # TODO: Validate each field, catching exceptions
    # TODO: Return list of error messages
    return errors


def validate_batch(records):
    """Validate all records and generate a report."""
    # TODO: Loop through records
    # TODO: Collect errors per record
    # TODO: Print summary report
    pass


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
