# Day 8: Log Analyzer
# Parse web server logs with regex and generate reports.

import re
from collections import Counter


def create_sample_log(filename="access.log"):
    """Create a sample log file for testing."""
    sample_lines = [
        '192.168.1.1 - - [17/Mar/2024:08:15:30 +0000] "GET /index.html HTTP/1.1" 200 5432',
        '192.168.1.1 - - [17/Mar/2024:08:15:31 +0000] "GET /style.css HTTP/1.1" 200 1234',
        '10.0.0.5 - - [17/Mar/2024:09:22:15 +0000] "POST /api/login HTTP/1.1" 401 89',
        '10.0.0.5 - - [17/Mar/2024:09:22:20 +0000] "POST /api/login HTTP/1.1" 200 445',
        '172.16.0.3 - - [17/Mar/2024:10:30:00 +0000] "GET /dashboard HTTP/1.1" 200 8901',
        '192.168.1.1 - - [17/Mar/2024:10:31:05 +0000] "GET /api/users HTTP/1.1" 200 2345',
        '10.0.0.5 - - [17/Mar/2024:11:00:00 +0000] "GET /nonexistent HTTP/1.1" 404 123',
        '172.16.0.3 - - [17/Mar/2024:11:15:30 +0000] "GET /api/data HTTP/1.1" 500 56',
        '192.168.1.100 - - [17/Mar/2024:12:00:00 +0000] "GET /index.html HTTP/1.1" 200 5432',
        '10.0.0.5 - - [17/Mar/2024:12:30:45 +0000] "DELETE /api/users/5 HTTP/1.1" 403 78',
        '192.168.1.1 - - [17/Mar/2024:13:00:00 +0000] "GET /index.html HTTP/1.1" 200 5432',
        '172.16.0.3 - - [17/Mar/2024:13:45:00 +0000] "PUT /api/users/3 HTTP/1.1" 200 234',
    ]
    with open(filename, "w") as f:
        f.write("\n".join(sample_lines))


# TODO: Define your regex pattern for parsing log lines
LOG_PATTERN = r""  # Build this step by step!


def parse_log_line(line):
    """Parse a single log line and return a dictionary of fields."""
    # TODO: Use re.search or re.match with your pattern
    # TODO: Return dict with: ip, timestamp, method, url, status, size
    # TODO: Return None for lines that don't match
    pass


def parse_log_file(filename):
    """Parse all lines in a log file."""
    entries = []
    # TODO: Read file line by line
    # TODO: Parse each line
    # TODO: Collect valid entries
    return entries


def generate_report(entries):
    """Generate and print the analysis report."""
    # TODO: Total requests
    # TODO: Top 5 IPs (use Counter)
    # TODO: Top 5 URLs
    # TODO: Status code breakdown
    # TODO: Requests per hour
    # TODO: Total bytes
    # TODO: Error rate
    pass


def main():
    import os
    if not os.path.exists("access.log"):
        create_sample_log()

    entries = parse_log_file("access.log")
    generate_report(entries)


if __name__ == "__main__":
    main()
