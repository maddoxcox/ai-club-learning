# Day 9: Email & Data Cleaner
# A regex-powered data cleaning toolkit.

import re


# --- Tool 1: Email Validator ---

# TODO: Compile your email regex pattern
# EMAIL_PATTERN = re.compile(r"...")

def validate_email(email):
    """Validate an email address. Return True/False."""
    # TODO: Use re.fullmatch with your pattern
    pass


def validate_email_batch(emails):
    """Validate a list of emails and report results."""
    # TODO: Check each email, print valid/invalid
    pass


# --- Tool 2: Phone Number Extractor ---

# TODO: Compile phone number pattern(s)
# PHONE_PATTERN = re.compile(r"...")

def extract_phones(text):
    """Extract all phone numbers from text."""
    # TODO: Use re.findall
    # TODO: Return list of found numbers
    pass


def normalize_phone(phone):
    """Normalize a phone number to (XXX) XXX-XXXX format."""
    # TODO: Strip all non-digits
    # TODO: Format consistently
    pass


# --- Tool 3: Text Cleaner ---

def clean_whitespace(text):
    """Replace multiple spaces/newlines with single space."""
    # TODO: Use re.sub
    pass


def redact_ssn(text):
    """Replace SSN patterns (XXX-XX-XXXX) with [REDACTED]."""
    # TODO: Use re.sub with SSN pattern
    pass


def clean_text(text):
    """Apply all cleaning operations."""
    # TODO: Chain all cleaners together
    pass


# --- Tool 4: URL Extractor ---

def extract_urls(text):
    """Extract all URLs from text."""
    # TODO: Use re.findall with URL pattern
    pass


# --- Interactive Menu ---

def main():
    """Main menu for the data cleaning toolkit."""
    while True:
        print("\n=== Data Cleaning Toolkit ===")
        print("[1] Validate email addresses")
        print("[2] Extract phone numbers from text")
        print("[3] Clean messy text")
        print("[4] Extract URLs from text")
        print("[5] Quit")

        choice = input("\nChoice: ").strip()

        # TODO: Handle each choice
        # TODO: Get input from user
        # TODO: Call appropriate function
        # TODO: Display results


if __name__ == "__main__":
    main()
