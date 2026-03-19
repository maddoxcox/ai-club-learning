# Day 9: Email & Data Cleaner

## What You're Building
A data cleaning toolkit with multiple tools: email validator, phone number extractor, pattern-based find-and-replace, and messy input cleaner. All powered by regular expressions.

## What You'll Learn
- `re.match()` vs `re.search()` vs `re.fullmatch()` — when to use which
- `re.sub()` — find and replace with regex
- Regex special characters — `.`, `+`, `*`, `?`, `[]`, `()`, `^`, `$`
- `re.compile()` — pre-compiling patterns for performance
- Real-world regex patterns — email, phone, URL validation

## Requirements
Build `data_cleaner.py` with these tools:

### Tool 1: Email Validator
- Validate email addresses against a robust pattern
- Handle: user@domain.com, first.last@company.co.uk, user+tag@gmail.com
- Reject: @domain.com, user@, user@@domain.com, user@.com

### Tool 2: Phone Number Extractor
- Extract ALL phone numbers from a block of text
- Handle formats: (555) 123-4567, 555-123-4567, 5551234567, +1-555-123-4567
- Normalize all to a consistent format: (555) 123-4567

### Tool 3: Text Cleaner
- Remove extra whitespace (multiple spaces → single space)
- Remove special characters but keep punctuation
- Fix common patterns: multiple periods → ellipsis, normalize quotes
- Redact sensitive data: replace SSN patterns (XXX-XX-XXXX) with [REDACTED]

### Tool 4: URL Extractor
- Find all URLs in a block of text
- Handle: http://, https://, www. prefixes
- Extract domain name separately

## Interactive Menu
Build a CLI menu that lets you pick which tool to use and input data interactively.

## How to Work
- Build one tool at a time
- Test each regex pattern in the Python REPL before putting it in code
- Use regex101.com to visualize your patterns

## Stretch Goals
- Add a batch mode: process a whole file of emails/text
- Add a regex builder: user describes what they want, you suggest a pattern
- Add support for international phone numbers

## When You're Done
```
git add .
git commit -m "Day 9: Data cleaning toolkit with regex"
git push
```
