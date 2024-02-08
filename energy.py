from faker import Faker
import pandas as pd
import random

fake = Faker()

# Function to generate Energy Consumption dataset
def generate_energy_consumption(num_records):
    data = {
        'ConsumerID': range(1, num_records + 1),
        'Location': [fake.city() for _ in range(num_records)],
        'Usage_KWh': [random.randint(100, 10000) for _ in range(num_records)],
        'Month': [fake.month_name() for _ in range(num_records)],
        'Year': [random.randint(2015, 2025) for _ in range(num_records)]
    }
    return pd.DataFrame(data)

# Function to generate Energy Production dataset
def generate_energy_production(num_records):
    data = {
        'ProductionID': range(1, num_records + 1),
        'Location': [fake.city() for _ in range(num_records)],
        'Production_KWh': [random.randint(1000, 100000) for _ in range(num_records)],
        'Month': [fake.month_name() for _ in range(num_records)],
        'Year': [random.randint(2015, 2025) for _ in range(num_records)]
    }
    return pd.DataFrame(data)

# Function to generate Energy Infrastructure dataset
def generate_energy_infrastructure(num_records):
    data = {
        'FacilityID': range(1, num_records + 1),
        'Location': [fake.city() for _ in range(num_records)],
        'Type': [random.choice(['Solar', 'Wind', 'Hydro', 'Nuclear']) for _ in range(num_records)],
        'Capacity_MW': [random.randint(1, 100) for _ in range(num_records)]
    }
    return pd.DataFrame(data)

# Function to generate Energy Grid dataset
def generate_energy_grid(num_records):
    data = {
        'GridID': range(1, num_records + 1),
        'From': [fake.city() for _ in range(num_records)],
        'To': [fake.city() for _ in range(num_records)],
        'Distance_km': [random.randint(10, 1000) for _ in range(num_records)],
        'Capacity_MW': [random.randint(100, 1000) for _ in range(num_records)]
    }
    return pd.DataFrame(data)

# Generate datasets
if __name__ == "__main__":
    num_records = 1000  # Number of records to generate

    energy_consumption_df = generate_energy_consumption(num_records)
    energy_production_df = generate_energy_production(num_records)
    energy_infrastructure_df = generate_energy_infrastructure(num_records)
    energy_grid_df = generate_energy_grid(num_records)

    # Save datasets to CSV
    path = "C:/Users/quindata/OneDrive/Bureau/energy/"
    energy_consumption_df.to_csv(path + 'energy_consumption.csv', index=False)
    energy_production_df.to_csv(path + 'energy_production.csv', index=False)
    energy_infrastructure_df.to_csv(path + 'energy_infrastructure.csv', index=False)
    energy_grid_df.to_csv(path + 'energy_grid.csv', index=False)
