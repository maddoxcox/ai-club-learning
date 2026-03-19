# Day 6: CSV Report Generator
# Read messy CSV data, clean it, generate a summary report.

import csv
import os


def create_sample_data(filename="sales_data.csv"):
    """Create sample sales data CSV for testing."""
    # TODO: Write sample CSV data to file
    # Include some messy data: inconsistent caps, whitespace, missing values, $ in prices
    pass


def read_sales_data(filename):
    """Read and clean sales data from CSV."""
    records = []
    # TODO: Open file with csv.DictReader
    # TODO: Clean each row:
    #   - Skip rows with missing critical fields
    #   - Strip whitespace from strings
    #   - Normalize category (lowercase)
    #   - Convert price string "$29.99" to float 29.99
    #   - Convert quantity to int
    return records


def calculate_stats(records):
    """Calculate statistics per category."""
    stats = {}
    # TODO: Group records by category
    # TODO: For each category calculate:
    #   - total_sales (price * quantity summed)
    #   - avg_price
    #   - num_transactions
    #   - highest_sale
    return stats


def write_report(stats, filename="report.csv"):
    """Write summary statistics to a CSV file."""
    # TODO: Use csv.DictWriter
    # TODO: Write header row
    # TODO: Write one row per category
    pass


def print_summary(stats):
    """Print a formatted summary to the terminal."""
    # TODO: Print a nice table-like summary
    pass


def main():
    # Create sample data if it doesn't exist
    if not os.path.exists("sales_data.csv"):
        create_sample_data()

    # Read, process, report
    records = read_sales_data("sales_data.csv")
    stats = calculate_stats(records)
    write_report(stats)
    print_summary(stats)


if __name__ == "__main__":
    main()
