# Day 6: CSV Report Generator

## What You're Building
A data processing tool that reads a messy CSV file of sales data, cleans it up, calculates statistics by category, and writes a clean summary report.

## What You'll Learn
- `open()` — reading and writing files
- `csv` module — `csv.reader`, `csv.DictReader`, `csv.DictWriter`
- `with` statement — safe file handling
- Data processing — cleaning, filtering, aggregating
- File paths and working directories

## Requirements
Build `csv_reporter.py` that:

1. **Reads `sales_data.csv`** (you'll create this sample data too)
2. **Cleans the data:**
   - Skip rows with missing values
   - Convert price strings like "$12.50" to floats
   - Normalize category names (lowercase, strip whitespace)
3. **Calculates per category:**
   - Total sales
   - Average sale price
   - Number of transactions
   - Highest single sale
4. **Writes `report.csv`** with the summary
5. **Prints a formatted summary** to the terminal

## Sample Data (create `sales_data.csv`)
```
date,product,category,price,quantity
2024-01-15,Widget A,Electronics,$29.99,3
2024-01-15,Gadget B,electronics,$49.99,1
2024-01-16,Shirt C, Clothing ,$19.99,2
2024-01-16,Widget D,Electronics,$34.99,
2024-01-17,,Food,$5.99,10
2024-01-17,Pants E,Clothing,$39.99,1
2024-01-18,Phone F,Electronics,$199.99,1
2024-01-18,Salad G,Food,$8.99,5
```
Notice: inconsistent capitalization, whitespace in categories, missing values, $ in prices.

## How to Work
- First create the sample CSV data
- Read it with csv.DictReader
- Build cleaning functions one at a time
- Calculate statistics using dictionaries
- Write the report

## Stretch Goals
- Accept the input filename as a command-line argument
- Support multiple input files
- Generate a bar chart of sales by category (using `matplotlib`)
- Handle additional CSV edge cases (quoted fields, different delimiters)

## When You're Done
```
git add .
git commit -m "Day 6: CSV Report Generator with data cleaning"
git push
```
