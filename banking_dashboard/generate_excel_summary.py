import pandas as pd

def generate_excel_summary(processed_csv="banking_dashboard/processed_transactions.csv", output_excel="banking_dashboard/summary_report.xlsx"):
    # Read processed data
    df = pd.read_csv(processed_csv)

    # Create a pivot table for summary
    pivot_table = pd.pivot_table(df, values='total_amount', index='month', columns='category', aggfunc='sum', fill_value=0)

    # Write to Excel
    with pd.ExcelWriter(output_excel) as writer:
        pivot_table.to_excel(writer, sheet_name='Monthly Category Summary')

    print(f"Excel summary report generated at {output_excel}")

if __name__ == "__main__":
    generate_excel_summary()
