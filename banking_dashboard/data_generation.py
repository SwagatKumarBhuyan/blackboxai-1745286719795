import pandas as pd
import numpy as np
from faker import Faker
import random

def generate_banking_data(num_rows=80000):
    fake = Faker()
    Faker.seed(0)
    np.random.seed(0)
    random.seed(0)

    # Generate data
    data = {
        "transaction_id": [fake.uuid4() for _ in range(num_rows)],
        "account_id": [fake.uuid4() for _ in range(num_rows)],
        "transaction_date": [fake.date_between(start_date='-2y', end_date='today') for _ in range(num_rows)],
        "transaction_type": np.random.choice(["deposit", "withdrawal", "payment", "transfer"], size=num_rows),
        "amount": np.round(np.random.uniform(10.0, 10000.0, size=num_rows), 2),
        "merchant": [fake.company() for _ in range(num_rows)],
        "category": np.random.choice(["groceries", "utilities", "entertainment", "travel", "salary", "loan", "others"], size=num_rows),
        "city": [fake.city() for _ in range(num_rows)],
        "state": [fake.state_abbr() for _ in range(num_rows)],
        "country": ["USA"] * num_rows
    }

    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = generate_banking_data()
    df.to_csv("banking_dashboard/banking_transactions.csv", index=False)
    print("Banking transactions data generated and saved to banking_dashboard/banking_transactions.csv")
