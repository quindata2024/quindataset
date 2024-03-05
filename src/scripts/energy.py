from faker import Faker
import pandas as pd
import random

fake = Faker()

# Function to generate Energy Consumption dataset
def generate_energy_consumption(num_records):
    data = {
        'ConsumerID': [f"C{str(i).zfill(3)}" for i in range(1, num_records + 1)],
        'Location': [fake.city() for _ in range(num_records)],
        'Usage_KWh': [random.randint(100, 10000) for _ in range(num_records)],
        'Month': [fake.month_name() for _ in range(num_records)],
        'Year': [random.randint(2010, 2025) for _ in range(num_records)]
    }
    return pd.DataFrame(data)

# Function to generate Energy Production dataset
def generate_energy_production(num_records):
    data = {
        'ProductionID': [f"P{str(i).zfill(3)}" for i in range(1, num_records + 1)],
        'Location': [fake.city() for _ in range(num_records)],
        'Production_KWh': [random.randint(1000, 100000) for _ in range(num_records)],
        'Month': [fake.month_name() for _ in range(num_records)],
        'Year': [random.randint(2010, 2025) for _ in range(num_records)]
    }
    return pd.DataFrame(data)

# Function to generate Energy Infrastructure dataset
def generate_energy_infrastructure(num_records):
    data = {
        'FacilityID': [f"F{str(i).zfill(3)}" for i in range(1, num_records + 1)],
        'Location': [fake.city() for _ in range(num_records)],
        'Type': [random.choice(['Solar', 'Wind', 'Hydro', 'Nuclear']) for _ in range(num_records)],
        'Capacity_MW': [random.randint(1, 100) for _ in range(num_records)]
    }
    return pd.DataFrame(data)

# Function to generate Energy Grid dataset
def generate_energy_grid(num_records):
    data = {
        'GridID': [f"G{str(i).zfill(3)}" for i in range(1, num_records + 1)],
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

    # Add common columns for linking tables
    energy_consumption_df['LocationID'] = 'L' + energy_consumption_df.groupby('Location').ngroup().astype(str).str.zfill(4)
    energy_production_df['LocationID'] = 'L' + energy_production_df.groupby('Location').ngroup().astype(str).str.zfill(4)
    energy_infrastructure_df['LocationID'] = 'L' + energy_infrastructure_df.groupby('Location').ngroup().astype(str).str.zfill(4)
    energy_grid_df['FromLocationID'] = 'L' + energy_grid_df.groupby('From').ngroup().astype(str).str.zfill(4)
    energy_grid_df['ToLocationID'] = 'L' + energy_grid_df.groupby('To').ngroup().astype(str).str.zfill(4)


    # Save datasets to CSV
    path = "C:/Users/njamo/OneDrive/Bureau/fakedata/energy/"
    energy_consumption_df.to_csv(path + 'energy_consumption_2.csv', index=False)
    energy_production_df.to_csv(path + 'energy_production_2.csv', index=False)
    energy_infrastructure_df.to_csv(path + 'energy_infrastructure_2.csv', index=False)
    energy_grid_df.to_csv(path + 'energy_grid_2.csv', index=False)
