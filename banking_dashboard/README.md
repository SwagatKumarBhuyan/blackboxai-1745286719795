# Banking Finance Dashboard Project

This project provides a comprehensive banking finance domain dashboard solution including data generation, SQL scripts, Python ETL, Excel summary, and instructions for Tableau and Power BI dashboards.

## Project Structure

- `data_generation.py`: Python script to generate synthetic banking transactions data (80,000+ rows).
- `banking_transactions.csv`: Generated CSV data file (after running data_generation.py).
- `create_load_sql.sql`: SQL script to create the banking transactions table and load data from CSV.
- `data_etl.py`: Python ETL script to process raw data and generate aggregated data.
- `processed_transactions.csv`: Processed data output (after running data_etl.py).
- `generate_excel_summary.py`: Python script to generate an Excel summary report from processed data.
- `summary_report.xlsx`: Excel summary report (after running generate_excel_summary.py).

## Usage Instructions

### 1. Generate Synthetic Data

Run the data generation script to create synthetic banking transactions data:

```bash
python3 data_generation.py
```

### 2. Load Data into Database

Use the `create_load_sql.sql` script to create the table and load data into your SQL database. Adjust the file path in the COPY command as needed.

### 3. Run ETL Process

Run the ETL script to process raw data and generate aggregated data:

```bash
python3 data_etl.py
```

### 4. Generate Excel Summary Report

Run the script to generate an Excel summary report:

```bash
python3 generate_excel_summary.py
```

### 5. Tableau Dashboard

- Use the `processed_transactions.csv` file as the data source.
- Create visualizations such as:
  - Monthly transaction amounts by category.
  - Transaction counts by category.
  - Trends over time.
- Use filters for transaction type, city, state, etc.

### 6. Power BI Dashboard

- Import the `processed_transactions.csv` file into Power BI.
- Create similar visualizations as in Tableau.
- Use slicers and filters for interactivity.

## Notes

- The synthetic data simulates banking transactions with various categories and locations.
- Adjust scripts as needed for your environment and database.
- For large datasets, ensure your database and tools can handle the data volume.

## Requirements

- Python 3.x
- pandas
- numpy
- faker
- Excel or compatible spreadsheet software
- Tableau Desktop (for Tableau dashboard)
- Power BI Desktop (for Power BI dashboard)

Install Python dependencies with:

```bash
pip install pandas numpy faker openpyxl
```

## Contact

For questions or support, please contact the project maintainer.
