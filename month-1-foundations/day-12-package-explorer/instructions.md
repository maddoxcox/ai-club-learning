# Day 12: Package Explorer

## What You're Building
A script that explores third-party Python packages. Install them, inspect their features, call their functions, and generate a mini usage report. Explore: `requests`, `rich`, and `click`.

## What You'll Learn
- `pip install` — how package management works
- Inspecting packages — `__version__`, `dir()`, `help()`
- `rich` — beautiful terminal output (tables, panels, progress bars)
- `click` — building professional CLIs
- Python "et cetera" — list comprehensions, walrus operator, unpacking, f-strings

## Requirements
Build `explorer.py` that:

1. **Inspects any installed package** — show version, main modules, docstring
2. **Demos 3 packages:**
   - **requests**: `.get()`, `.post()`, response objects, status codes
   - **rich**: Console, Table, Panel, Progress
   - **click**: `@click.command()`, `@click.option()`, `@click.argument()`
3. **Python Et Cetera Practice:**
   - List comprehensions: `[x**2 for x in range(10)]`
   - Dict comprehensions
   - Walrus operator: `if (n := len(data)) > 10:`
   - Unpacking: `first, *rest = my_list`
   - f-strings with formatting: `f"{price:.2f}"`

## Setup
```
pip install requests rich click
```

## Stretch Goals
- Build a general-purpose package inspector for ANY pip package
- Create a `click` CLI that wraps your previous projects

## When You're Done
```
git add . && git commit -m "Day 12: Package Explorer - requests, rich, click" && git push
```
