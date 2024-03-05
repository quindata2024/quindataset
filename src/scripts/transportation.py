import pandas as pd
import numpy as np
from faker import Faker

# Set up Faker for realistic data generation
fake = Faker()

# Define parent tables

# Locations (cities, airports, stations, etc.)
locations = pd.DataFrame({
    "location_id": [f"L{str(i).zfill(2)}" for i in range(1, 51)],
    "name": [fake.city() for _ in range(50)],
    "country": np.random.choice(["US", "Canada", "UK"], 50, replace=True),
    "latitude": np.random.uniform(20, 50, 50),
    "longitude": np.random.uniform(-120, -60, 50)
})

# Define lists of vehicle models for each type
car_models = ["Toyota Camry", "Honda Civic", "Ford F-150", "Chevrolet Silverado", "Nissan Altima", "Tesla Model S", "BMW 3 Series", "Mercedes-Benz C-Class", "Audi A4", "Volkswagen Jetta"]
bus_models = ["Volvo 9700", "New Flyer Xcelsior", "Gillig Low Floor", "BYD K9", "Irizar i8", "MAN Lion's City", "Scania Citywide", "Nova Bus LFS", "Blue Bird Vision", "Neoplan Tourliner"]
train_models = ["Bombardier Talent", "Siemens Velaro", "Alstom Coradia", "Stadler FLIRT", "Hitachi A-Train", "CRRC Qingdao Sifang", "Talgo Avril", "CAF Oaris", "Kawasaki N700 Series Shinkansen", "AnsaldoBreda Trenitalia Frecciargento"]
airplane_models = ["Boeing 737", "Airbus A320", "Boeing 787 Dreamliner", "Airbus A380", "Embraer E-Jet", "Bombardier CRJ Series", "Boeing 777", "Airbus A350 XWB", "Boeing 747", "Bombardier Dash 8"]

# Generate vehicle types
veh = np.random.choice(["Car", "Bus", "Train", "Airplane"], 100, replace=True)

# Create the DataFrame with modified capacity ranges
vehicles = pd.DataFrame({
    "vehicle_id": [f"V{str(i).zfill(3)}" for i in range(1, 101)],
    "type": veh,
    "capacity": [np.random.randint(2, 6) if t == "Car" else
                 np.random.randint(30, 71) if t == "Bus" else
                 np.random.randint(80, 301) if t == "Airplane" else
                 np.random.randint(301, 1001) for t in veh],
    "model": [np.random.choice(car_models) if t == "Car" else
              np.random.choice(bus_models) if t == "Bus" else
              np.random.choice(train_models) if t == "Train" else
              np.random.choice(airplane_models) for t in veh]
})

# Define child tables linked to parent tables

# Trips (journeys with origin, destination, vehicle, etc.)
trips = pd.DataFrame({
    "trip_id": [f"T{str(i).zfill(3)}" for i in range(1, 501)],
    "origin_location_id": np.random.choice(locations["location_id"], 500, replace=True),
    "destination_location_id": np.random.choice(locations["location_id"], 500, replace=True),
    "vehicle_id": np.random.choice(vehicles["vehicle_id"], 500, replace=True),
    "start_date": pd.to_datetime([fake.date_between(start_date="-2y", end_date="today") for _ in range(500)])
})

# Passengers (traveling on specific trips)
passengers = pd.DataFrame({
    "passenger_id": [f"P{str(i).zfill(4)}" for i in range(1, 1001)],
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
path = "C:/Users/OneDrive/Bureau/transportation/"
locations.to_csv(path + "locations.csv")
vehicles.to_csv(path + "vehicles.csv")
trips.to_csv(path + "trips.csv")
passengers.to_csv(path + "passengers.csv")

