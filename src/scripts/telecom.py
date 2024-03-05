import pandas as pd
import numpy as np
from faker import Faker

# Set up Faker for realistic data generation
fake = Faker()

# Define parent tables

# Customers (mobile phone users)
customers = pd.DataFrame({
    "customer_id": [f"C{str(i).zfill(3)}" for i in range(1, 1001)],
    "name": [fake.name() for _ in range(1000)],
    "phone_number": [fake.phone_number() for _ in range(1000)],
    "address": [fake.address() for _ in range(1000)],
    "plan": np.random.choice(["Prepaid", "Postpaid"], 1000, replace=True)
})

# Define child tables linked to parent tables

# Mobile lines (subscriptions associated with phones)
mobile_lines = pd.DataFrame({
    "line_id": [f"L{str(i).zfill(3)}" for i in range(1, 1001)],
    "customer_id": np.random.choice(customers["customer_id"], 1000, replace=True),
    "number": np.random.choice(customers["phone_number"], 1000, replace=True),  # Match customer numbers
    "activation_date": pd.to_datetime([fake.date_between(start_date="-5y", end_date="today") for _ in range(1000)])
})

# Calls (mobile voice calls between users)
calls = pd.DataFrame({
    "call_id": [f"CAL{str(i).zfill(4)}" for i in range(1, 10001)],
    "calling_line_id": np.random.choice(mobile_lines["line_id"], 10000, replace=True),
    "called_line_id": np.random.choice(mobile_lines["line_id"], 10000, replace=True),  # Allow self-calls
    "start_time": pd.to_datetime([fake.date_between(start_date="-5y", end_date="today") for _ in range(10000)]),
    "duration": np.random.randint(30, 3600, 10000)  # Seconds (1 min - 1 hour)
})

# Generate SMS content
def generate_sms_content():
    greetings = ["Hi", "Hey", "Hello"]
    questions = ["How are you?", "What's up?", "How's it going?"]
    responses = ["I'm good, thanks!", "Not much, just chilling.", "Everything's great, thanks for asking!"]
    actions = ["Let's catch up soon!", "Wanna grab coffee sometime?", "We should hang out!"]

    # Randomly select a pattern
    pattern = np.random.choice(["greetings", "questions", "responses", "actions"], p=[0.4, 0.2, 0.2, 0.2])

    if pattern == "greetings":
        return np.random.choice(greetings)
    elif pattern == "questions":
        return np.random.choice(questions)
    elif pattern == "responses":
        return np.random.choice(responses)
    else:
        return np.random.choice(actions)

# Generate SMS DataFrame
sms = pd.DataFrame({
    "message_id": [f"M{str(i).zfill(4)}" for i in range(1, 20001)],
    "sender_line_id": np.random.choice(mobile_lines["line_id"], 20000, replace=True),
    "recipient_line_id": np.random.choice(mobile_lines["line_id"], 20000, replace=True),
    "send_time": pd.to_datetime([fake.date_between(start_date="-4y", end_date="today") for _ in range(20000)]),
    "content": [generate_sms_content() for _ in range(20000)]
})

# Data usage (internet data consumed by users)
data_usage = pd.DataFrame({
    "usage_id": [f"U{str(i).zfill(3)}" for i in range(1, 5001)],
    "line_id": np.random.choice(mobile_lines["line_id"], 5000, replace=True),
    "usage_date": pd.to_datetime([fake.date_between(start_date="-4y", end_date="today") for _ in range(5000)]),
    "data_amount": np.random.randint(100, 10000, 5000)  # MB
})

# Create relationships between tables using foreign keys
customers = customers.set_index("customer_id")
mobile_lines = mobile_lines.set_index("line_id")
calls = calls.set_index(["calling_line_id", "called_line_id", "start_time"])
sms = sms.set_index(["sender_line_id", "recipient_line_id", "send_time"])
data_usage = data_usage.set_index(["line_id", "usage_date"])

# save the dataset to files CSV
path = "C:/Users/OneDrive/Bureau/telecom/"
customers.to_csv(path + "customers.csv")
mobile_lines.to_csv(path + "mobile_lines.csv")
calls.to_csv(path + "calls.csv")
sms.to_csv(path + "sms.csv")
data_usage.to_csv(path + "data_usage.csv")
