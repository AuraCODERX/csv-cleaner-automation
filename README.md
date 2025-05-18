# CSV Cleaner & Reporter Tool

A powerful and user-friendly Python-based automation tool that **cleans messy CSV files** and generates a **rich visual report** in the terminal — perfect for analysts, data scientists, and businesses dealing with large datasets.

---

## Features

- **Automatic Removal** of:
  - Duplicate rows
  - Fully empty rows
- **Data Summary Report** including:
  - Total rows & columns before and after cleaning
  - Number of missing values
  - Column with most null values
  - Column with most unique values
- **Rich Terminal Interface** using `rich` module for beautiful, color-coded output
- **Auto-saves cleaned file** with timestamp to avoid overwriting original data
- Clean **top 5 sample rows** displayed in a stylish panel
- Full error handling with clear feedback in console

---

## How to Use

1. **Run the script** in any Python 3 environment:
   ```bash
   python csv_cleaner.py
