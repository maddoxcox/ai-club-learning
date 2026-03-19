# Day 1: Grade Calculator

## What You're Building
A command-line GPA calculator. The user enters grades one at a time, and your program calculates their GPA. The catch: it must handle EVERY type of bad input without crashing.

## What You'll Learn (by building, not reading)
- `try` / `except` blocks
- `ValueError`, `TypeError`, `KeyError`
- `while` loops for retrying after bad input
- Input validation patterns
- Graceful error messages (not tracebacks)

## Setup
1. Sign up for GitHub Student Developer Pack: https://education.github.com/pack
2. Create a new GitHub repo called `ai-club-learning`
3. Clone it to your machine

## Requirements
Build `grade_calculator.py` that:

1. **Prompts for grades** — Ask the user to enter letter grades (A, B, C, D, F) one at a time
2. **Converts to GPA points** — A=4.0, B=3.0, C=2.0, D=1.0, F=0.0
3. **Handles bad input:**
   - What if they type "Z"? (not a valid grade)
   - What if they type a number instead?
   - What if they just press Enter with nothing?
   - What if they type "a" lowercase? (should still work)
4. **Calculates GPA** — After they type "done", show the average
5. **Handles edge cases:**
   - What if they type "done" without entering any grades?
   - What if they want to quit mid-way? (Ctrl+C should exit cleanly)

## How to Work
- Open this folder in your terminal
- Tell Claude Code: "Let's build this grade calculator. Start with the basic structure."
- Build it piece by piece — get the happy path working first, then add error handling

## Stretch Goals
- Add +/- support (A+ = 4.0, A- = 3.7, B+ = 3.3, etc.)
- Add credit hours (weighted GPA)
- Color the output (green for good GPA, red for bad) using the `rich` library

## When You're Done
```
git add .
git commit -m "Day 1: Grade Calculator with error handling"
git push
```
