import pandas as pd
import numpy as np
import random
from faker import Faker

# Set up Faker for realistic data generation
fake = Faker()

# Define parent tables

# Customers (mobile phone users)
customers = pd.DataFrame({
    "customer_id": np.arange(1000),
    "name": [fake.name() for _ in range(1000)],
    "phone_number": [fake.phone_number() for _ in range(1000)],
    # Replace with anonymized versions:
    "address": [fake.address() for _ in range(1000)],
    "plan": np.random.choice(["Prepaid", "Postpaid"], 1000, replace=True)
})

# Define child tables linked to parent tables

# Mobile lines (subscriptions associated with phones)
mobile_lines = pd.DataFrame({
    "line_id": np.arange(1000),
    "customer_id": np.random.choice(customers["customer_id"], 1000, replace=True),
    "number": np.random.choice(customers["phone_number"], 1000, replace=True),  # Match customer numbers
    "activation_date": pd.to_datetime([fake.date_between(start_date="-2y", end_date="today") for _ in range(1000)])
})

# Calls (mobile voice calls between users)
calls = pd.DataFrame({
    "call_id": np.arange(10000),
    "calling_line_id": np.random.choice(mobile_lines["line_id"], 10000, replace=True),
    "called_line_id": np.random.choice(mobile_lines["line_id"], 10000, replace=True),  # Allow self-calls
    "start_time": pd.to_datetime([fake.date_time_between(start_date="-1y", end_date="-2y") for _ in range(10000)]),
    "duration": np.random.randint(30, 3600, 10000)  # Seconds (1 min - 1 hour)
})

# SMS messages (text messages between users)
sms = pd.DataFrame({
    "message_id": np.arange(20000),
    "sender_line_id": np.random.choice(mobile_lines["line_id"], 20000, replace=True),
    "recipient_line_id": np.random.choice(mobile_lines["line_id"], 20000, replace=True),
    "send_time": pd.to_datetime([fake.date_time_between(start_date="-1y", end_date="-2y") for _ in range(20000)]),
    "content": [fake.sentence(nb_words=10) for _ in range(20000)]
})

# Data usage (internet data consumed by users)
data_usage = pd.DataFrame({
    "usage_id": np.arange(5000),
    "line_id": np.random.choice(mobile_lines["line_id"], 5000, replace=True),
    "usage_date": pd.to_datetime([fake.date_time_between(start_date="-1y", end_date="-2y") for _ in range(5000)]),
    "data_amount": np.random.randint(100, 10000, 5000)  # MB
})

# Create relationships between tables using foreign keys
customers = customers.set_index("customer_id")
mobile_lines = mobile_lines.set_index("line_id")
calls = calls.set_index(["calling_line_id", "called_line_id", "start_time"])
sms = sms.set_index(["sender_line_id", "recipient_line_id", "send_time"])
data_usage = data_usage.set_index(["line_id", "usage_date"])

# save the dataset to files CSV
path = "C:/Users/quindata/OneDrive/Bureau/telecom/"
customers.to_csv(path + "customers.csv")
mobile_lines.to_csv(path + "mobile_lines.csv")
calls.to_csv(path + "calls.csv")
sms.to_csv(path + "sms.csv")
data_usage.to_csv(path + "data_usage.csv")
