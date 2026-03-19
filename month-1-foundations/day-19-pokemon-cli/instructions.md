# Day 19: Pokemon CLI (Python)

## What You're Building
The same Pokemon tool, but in Python. Compare how JS fetch (async) and Python requests (sync) handle the same task.

## What You'll Learn
- `requests.get()` — Python's HTTP client
- `response.json()` and `response.status_code`
- Error handling — network errors, API errors, timeouts
- JSON file caching — save fetched data locally
- Python vs JavaScript comparison

## Requirements
1. **Search:** `python pokemon_cli.py pikachu`
2. **Display:** name, ID, types, stats (with ASCII bar charts), abilities
3. **Error handling:** not found, no internet, timeout
4. **JSON cache:** save to `cache/{name}.json`, load from cache on repeat
5. **Compare mode:** `python pokemon_cli.py pikachu charizard`

## After Building — Compare Python vs JS:
- `requests.get()` is synchronous — blocks until done
- `fetch()` is asynchronous — returns a Promise
- How does error handling differ?
- Which felt more natural?

## Stretch Goals
- `--random` flag
- `--type fire` to list Pokemon by type
- `rich` library for colorful output

## When You're Done
```
git add . && git commit -m "Day 19: Pokemon CLI with Python requests" && git push
```
