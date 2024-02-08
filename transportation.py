import pandas as pd
import numpy as np
import random
from faker import Faker

# Set up Faker for realistic data generation
fake = Faker()

# Define parent tables

# Locations (cities, airports, stations, etc.)
locations = pd.DataFrame({
    "location_id": np.arange(50),
    "name": [fake.city() for _ in range(50)],
    "country": np.random.choice(["US", "Canada", "Mexico"], 50, replace=True),
    "latitude": np.random.uniform(20, 50, 50),
    "longitude": np.random.uniform(-120, -60, 50)  # Adjust for relevant region
})

# Vehicles (cars, buses, trains, airplanes, etc.)
vehicles = pd.DataFrame({
    "vehicle_id": np.arange(100),
    "type": np.random.choice(["Car", "Bus", "Train", "Airplane"], 100, replace=True),
    "capacity": np.random.randint(10, 200, 100),
    "model": [fake.word() for _ in range(100)]
})

# Define child tables linked to parent tables

# Trips (journeys with origin, destination, vehicle, etc.)
trips = pd.DataFrame({
    "trip_id": np.arange(500),
    "origin_location_id": np.random.choice(locations["location_id"], 500, replace=True),
    "destination_location_id": np.random.choice(locations["location_id"], 500, replace=True),
    "vehicle_id": np.random.choice(vehicles["vehicle_id"], 500, replace=True),
    "start_date": pd.to_datetime([fake.date_between(start_date="-2y", end_date="today") for _ in range(500)])
})

# Passengers (traveling on specific trips)
passengers = pd.DataFrame({
    "passenger_id": np.arange(1000),
    "trip_id": np.random.choice(trips["trip_id"], 1000, replace=True),
    "name": [fake.name() for _ in range(1000)],
    "age": np.random.randint(18, 80, 1000),
    "origin": np.random.choice(["Airport", "Bus Station", "Train Station", "Other"], 1000, replace=True)
})

# Create relationships between tables using foreign keys
locations = locations.set_index("location_id")
vehicles = vehicles.set_index("vehicle_id")
trips = trips.set_index(["origin_location_id", "destination_location_id", "start_date"])
passengers = passengers.set_index(["trip_id", "passenger_id"])

# save the dataset to files CSV
path = "C:/Users/quindata/OneDrive/Bureau/transportation/"
locations.to_csv(path + "locations.csv")
vehicles.to_csv(path + "vehicles.csv")
trips.to_csv(path + "trips.csv")
passengers.to_csv(path + "passengers.csv")

