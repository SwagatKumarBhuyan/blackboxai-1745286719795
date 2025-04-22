import pandas as pd

def etl_process(input_csv="banking_dashboard/banking_transactions.csv", output_csv="banking_dashboard/processed_transactions.csv"):
    # Read raw data
    df = pd.read_csv(input_csv, parse_dates=['transaction_date'])

    # Example transformation: filter transactions in the last year
    last_year = pd.Timestamp.now() - pd.DateOffset(years=1)
    df_filtered = df[df['transaction_date'] >= last_year]

    # Example aggregation: total amount by category and month
    df_filtered['month'] = df_filtered['transaction_date'].dt.to_period('M')
    agg_df = df_filtered.groupby(['month', 'category']).agg(total_amount=('amount', 'sum'),
                                                           transaction_count=('transaction_id', 'count')).reset_index()

    # Save processed data
    agg_df.to_csv(output_csv, index=False)
    print(f"Processed data saved to {output_csv}")

if __name__ == "__main__":
    etl_process()
