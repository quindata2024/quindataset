import pandas as pd
import numpy as np
import faker
import random

# Create a Faker instance for realistic data generation
fake = faker.Faker()

# Define parent tables
customers = pd.DataFrame({
    "customer_id": np.arange(100),
    "name": [fake.name() for _ in range(100)],
    "address": [fake.address() for _ in range(100)],
    "phone_number": [fake.phone_number() for _ in range(100)],
    "email": [fake.email() for _ in range(100)],
    "social_security_number": [f"{fake.pyint(min_value=100000000, max_value=999999999)}" for _ in range(100)]  
})

# Ensure all column lengths are consistent:
customer_ids = np.arange(100).tolist()
account_types = ["Savings", "Checking", "Investment"] * 66
balances = np.random.randint(1000, 100000, 100).tolist()

accounts = pd.DataFrame({
    "account_id": np.arange(200),
    "customer_id": np.random.choice(customer_ids, 200, replace=True),
    "account_type": np.random.choice(account_types, 200, replace=True),
    "balance": np.random.choice(balances, 200, replace=True)
})

# Define child tables linked to parent tables

date_list = [fake.date_between(start_date="-2y", end_date="today") for _ in range(500)]
dates = np.repeat(date_list, 166)  # Repeat each date 166 times

# Repeated list to match desired length
transaction_types = ["Deposit", "Withdrawal", "Transfer"] * 27666 + ["Withdrawal", "Transfer"]

transactions = pd.DataFrame({
    "transaction_id": np.repeat(np.arange(500), 166),
    "account_id": np.tile(np.random.choice(accounts["account_id"], 500, replace=True), 166),
    "transaction_type": transaction_types,
    "amount": np.repeat(np.random.randint(-1000, 5000, 500), 166),
    "date": pd.to_datetime(dates)
})

investments = pd.DataFrame({
    "investment_id": np.arange(150),
    "account_id": np.random.choice(accounts["account_id"], 150, replace=True),
    "symbol": [fake.word() for _ in range(150)],
    "shares": np.random.randint(10, 1000, 150),
    "purchase_price": np.random.randint(10, 100, 150),
    "current_price": np.random.randint(5, 150, 150)
})

# Create relationships between tables using foreign keys
customers = customers.set_index("customer_id")
accounts = accounts.set_index("account_id")
transactions = transactions.set_index(["account_id", "transaction_id"])
investments = investments.set_index(["account_id", "investment_id"])

# save the dataset to files CSV
path = "C:/Users/quindata/OneDrive/Bureau/finance/"
customers.to_csv(path + "customers.csv")
accounts.to_csv(path + "accounts.csv")
transactions.to_csv(path + "transactions.csv")
investments.to_csv(path + "investments.csv")
