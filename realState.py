import pandas as pd
import numpy as np
import random
from faker import Faker

# Set up Faker for realistic data generation
fake = Faker()

# Define parent tables

# Properties (residential and commercial)
properties = pd.DataFrame({
    "property_id": np.arange(1000),
    "type": np.random.choice(["Residential", "Commercial"], 1000, replace=True),
    "address": [fake.address() for _ in range(1000)],
    "city": [fake.city() for _ in range(1000)],
    "state": [fake.state_abbr() for _ in range(1000)],
    "zip_code": np.random.randint(10000, 99999, 1000),
    "bedrooms": np.random.randint(1, 6, 1000),
    "bathrooms": np.random.randint(1, 4, 1000),
    "square_footage": np.random.randint(500, 5000, 1000),
    "year_built": np.random.randint(1950, 2025, 1000),
    "price": np.random.randint(100000, 10000000, 1000)
})

# Define child tables linked to parent tables

# Listings (properties being offered for sale or rent)
listings = pd.DataFrame({
    "listing_id": np.arange(2000),
    "property_id": np.random.choice(properties["property_id"], 2000, replace=True),
    "list_date": pd.to_datetime([fake.date_between(start_date="-1y", end_date="today") for _ in range(2000)]),
    "status": np.random.choice(["Active", "Pending", "Sold", "Leased"], 2000, replace=True),
    "list_price": np.random.randint(properties["price"].min(), properties["price"].max(), 2000),
    "listing_agent": [fake.name() for _ in range(2000)],
    "description": [fake.text(max_nb_chars=500) for _ in range(2000)]
})

# Transactions (completed sales or rentals)
transactions = pd.DataFrame({
    "transaction_id": np.arange(500),
    "listing_id": np.random.choice(listings[listings["status"] == "Sold"]["listing_id"], 500, replace=True),
    "sale_date": pd.to_datetime([fake.date_between(start_date="-6m", end_date="today") for _ in range(500)]),
    "sale_price": np.random.randint(0.9 * listings["list_price"].min(), 1.1 * listings["list_price"].max(), 500),
    "buyer_name": [fake.name() for _ in range(500)],
    "seller_name": [properties["address"].tolist() for _ in range(500)]  # Using property address as seller reference
})


# Create relationships between tables using foreign keys
properties = properties.set_index("property_id")
listings = listings.set_index("listing_id")
transactions = transactions.set_index("transaction_id")

# save the dataset to files CSV
path = "C:/Users/quindata/OneDrive/Bureau/realstate/"
properties.to_csv(path + "properties.csv")
listings.to_csv(path + "listings.csv")
transactions.to_csv(path + "transactions.csv")
