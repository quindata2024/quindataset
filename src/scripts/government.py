from faker import Faker
import pandas as pd
import random

fake = Faker()

# Function to generate Citizens dataset
def generate_citizens(num_records):
    data = {
        'CitizenID': [f"{fake.pyint(min_value=100000000, max_value=999999999)}" for _ in range(num_records)],
        'Name': [fake.name() for _ in range(num_records)],
        'Age': [random.randint(18, 80) for _ in range(num_records)],
        'AddressID':  [random.choice([f"A{str(i).zfill(3)}" for i in range(1, num_records + 1)]) for _ in range(num_records)],
        'TaxID': [random.choice([f"T{str(i).zfill(3)}" for i in range(1, num_records + 1)]) for _ in range(num_records)]
    }
    return pd.DataFrame(data)

# Function to generate Addresses dataset
def generate_addresses(num_records):
    data = {
        'AddressID': [f"A{str(i).zfill(3)}" for i in range(1, num_records + 1)],
        'Address': [fake.address() for _ in range(num_records)],
        'City': [fake.city() for _ in range(num_records)],
        'State': [fake.state() for _ in range(num_records)],
        'ZipCode': [fake.zipcode() for _ in range(num_records)]
    }
    return pd.DataFrame(data)

# Function to generate Taxes dataset
def generate_taxes(num_records):
    data = {
        'TaxID': [f"T{str(i).zfill(3)}" for i in range(1, num_records + 1)],
        'Year': [random.randint(2010, 2025) for _ in range(num_records)],
        'Amount': [random.uniform(1000, 10000) for _ in range(num_records)]
    }
    return pd.DataFrame(data)

# Generate datasets
if __name__ == "__main__":
    num_records = 1000  # Number of records to generate

    citizens_df = generate_citizens(num_records)
    addresses_df = generate_addresses(num_records)
    taxes_df = generate_taxes(num_records)

    # Save datasets to CSV
    path = "C:/Users/OneDrive/Bureau/government/"
    citizens_df.to_csv(path + 'citizens.csv', index=False)
    addresses_df.to_csv(path + 'addresses.csv', index=False)
    taxes_df.to_csv(path + 'taxes.csv', index=False)
