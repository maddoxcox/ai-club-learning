# Day 8: Log Analyzer

## What You're Building
A tool that parses web server log files (Apache/nginx format), extracts meaningful data using regular expressions, and generates a summary report.

## What You'll Learn
- `re` module — Python's regex library
- Regex patterns — `\d+`, `\w+`, `[]`, `()`, `.`, `*`, `+`
- `re.search()` and `re.findall()` — finding patterns
- Named groups — `(?P<name>pattern)`
- Pattern design — building regex step by step

## Requirements
Build `log_analyzer.py` that:

1. **Parses log entries** in this format:
   ```
   192.168.1.1 - - [17/Mar/2024:10:15:30 +0000] "GET /index.html HTTP/1.1" 200 1234
   10.0.0.5 - - [17/Mar/2024:10:15:31 +0000] "POST /api/login HTTP/1.1" 401 89
   ```

2. **Extracts from each line:**
   - IP address
   - Timestamp (date and hour)
   - HTTP method (GET, POST, etc.)
   - URL path
   - Status code
   - Response size (bytes)

3. **Generates a report:**
   - Total requests
   - Top 5 IP addresses (by request count)
   - Top 5 most visited URLs
   - Status code breakdown (how many 200s, 404s, 500s)
   - Requests per hour (busiest hours)
   - Total bytes transferred
   - Error rate (% of 4xx and 5xx responses)

4. **Creates sample log data** if no file is provided

## How to Work
- First, study the log format and design your regex pattern on paper
- Build and test the regex in Python's REPL first
- Then build the parser
- Then build the statistics functions

## Regex Hint
A good starting pattern uses named groups:
```python
pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+).*\[(?P<timestamp>.*?)\].*"(?P<method>\w+) (?P<url>\S+).*" (?P<status>\d+) (?P<size>\d+)'
```
Build it up piece by piece — don't try to write it all at once!

## Stretch Goals
- Parse and handle different log formats (detect format automatically)
- Generate an HTML report with charts
- Real-time monitoring mode (watch a log file for new entries)

## When You're Done
```
git add .
git commit -m "Day 8: Log Analyzer with regex parsing"
git push
```
