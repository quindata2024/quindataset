import pandas as pd
import numpy as np
import random
from faker import Faker

# Set up Faker for realistic data generation
fake = Faker()

# Define parent tables
customers = pd.DataFrame({
    "customer_id": np.arange(100),
    "name": [fake.name() for _ in range(100)],
    "email": [fake.email() for _ in range(100)],
    "phone_number": [fake.phone_number() for _ in range(100)],
    "address": [fake.address() for _ in range(100)]
})

products = pd.DataFrame({
    "product_id": np.arange(50),
    "name": [fake.word() + " " + fake.word() for _ in range(50)],
    "category": np.random.choice(["Electronics", "Clothing", "Home", "Beauty", "Toys"], 50, replace=True),
    "description": [fake.text(max_nb_chars=200) for _ in range(50)],
    "price": np.random.randint(10, 1000, 50)
})

# Ensure all column lengths are consistent
customer_ids = np.arange(100).tolist()

# Define child tables linked to parent tables
orders = pd.DataFrame({
    "order_id": np.arange(200),
    "customer_id": np.random.choice(customer_ids, 200, replace=True),
    "order_date": pd.to_datetime([fake.date_between(start_date="-1y", end_date="today") for _ in range(200)])
})

# Sample random number of products per order
num_products_per_order = np.random.randint(1, 5, 200)

# Create order details table
order_details = pd.DataFrame({
    "order_id": np.repeat(orders["order_id"], num_products_per_order),
    "product_id": np.random.choice(products["product_id"], sum(num_products_per_order), replace=True),
    "quantity": np.random.randint(1, 5, sum(num_products_per_order))
})


# Create relationships between tables using foreign keys
customers = customers.set_index("customer_id")
products = products.set_index("product_id")
orders = orders.set_index("order_id")
order_details = order_details.set_index(["order_id", "product_id"])

# save the dataset to files CSV
path = "C:/Users/quindata/OneDrive/Bureau/ecommerce/"
customers.to_csv(path + "customers.csv")
products.to_csv(path + "products.csv")
orders.to_csv(path + "orders.csv")
order_details.to_csv(path + "order_details.csv")

