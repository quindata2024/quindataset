import pandas as pd
import numpy as np
import random
from faker import Faker

# Set up Faker for realistic data generation
fake = Faker()

# Define parent tables

# Properties (residential and commercial)
properties = pd.DataFrame({
    "property_id": [f"P{str(i).zfill(3)}" for i in range(1, 1001)],
    "type": np.random.choice(["Residential", "Commercial"], 1000, replace=True),
    "address": [fake.address() for _ in range(1000)],
    "city": [fake.city() for _ in range(1000)],
    "state": [fake.state_abbr() for _ in range(1000)],
    "zip_code": np.random.randint(10000, 99999, 1000),
    "bedrooms": np.random.randint(1, 6, 1000),
    "bathrooms": np.random.randint(1, 4, 1000),
    "square_footage": np.random.randint(500, 5000, 1000),
    "year_built": np.random.randint(1950, 2024, 1000),
    "price": np.random.randint(1000000, 100000000, 1000)
})

# Define child tables linked to parent tables

# Define common property features
property_features = [
    "spacious living room",
    "modern kitchen with stainless steel appliances",
    "hardwood floors throughout",
    "large backyard with patio",
    "scenic views",
    "luxurious master suite",
    "updated bathrooms",
    "finished basement",
    "high ceilings",
    "attached garage",
    "energy-efficient windows",
    "central air conditioning",
    "walk-in closets",
    "open floor plan",
    "fireplace",
    "landscaped garden",
    "deck or balcony",
    "granite countertops",
    "stainless steel appliances",
    "vaulted ceilings",
    "natural light",
    "granite vanity tops",
    "separate laundry room",
    "covered porch",
    "security system",
    "fire pit",
    "home office space",
    "bonus room",
    "custom cabinetry",
    "breakfast nook",
    "formal dining room",
    "built-in shelving",
    "skylights",
    "fenced yard",
    "pantry",
    "french doors",
    "stone countertops",
    "pool with sundeck",
    "guest suite",
    "wine cellar",
    "home theater",
    "playroom",
    "exercise room",
    "wet bar",
    "game room",
    "sauna",
    "hot tub"
]

# Generate property descriptions
property_descriptions = [
    f"This beautiful home features {', '.join(random.sample(property_features, k=random.randint(3, 8)))}.",
    f"Spacious layout with {random.choice(property_features)} and {random.choice(property_features)}.",
    f"Charming property offering {', '.join(random.sample(property_features, k=random.randint(2, 5)))}.",
    f"Stunning {random.choice(property_features)} and {random.choice(property_features)} highlight this home's appeal.",
    f"Enjoy the {random.choice(property_features)} and {random.choice(property_features)} in this lovely property.",
    f"Modern design with {', '.join(random.sample(property_features, k=random.randint(3, 7)))}.",
    f"Relax in the {random.choice(property_features)} or entertain in the {random.choice(property_features)} of this home.",
    f"Classic architecture meets contemporary style in this property featuring {', '.join(random.sample(property_features, k=random.randint(3, 8)))}.",
    f"Impeccably maintained home with {random.choice(property_features)} and {random.choice(property_features)}.",
    f"This property boasts {', '.join(random.sample(property_features, k=random.randint(4, 9)))}."
]

# Listings (properties being offered for sale or rent)
listings = pd.DataFrame({
    "listing_id": [f"L{str(i).zfill(3)}" for i in range(1, 2001)],
    "property_id": np.random.choice(properties["property_id"], 2000, replace=True),
    "list_date": pd.to_datetime([fake.date_between(start_date="-2y", end_date="today") for _ in range(2000)]),
    "status": np.random.choice(["Active", "Pending", "Sold", "Leased"], 2000, replace=True),
    "list_price": np.random.randint(properties["price"].min(), properties["price"].max(), 2000),
    "listing_agent": [fake.name() for _ in range(2000)],
    "description": random.choices(property_descriptions, k=2000)
})

# Transactions (completed sales or rentals)
transactions = pd.DataFrame({
    "transaction_id": [f"T{str(i).zfill(2)}" for i in range(1, 501)],
    "listing_id": np.random.choice(listings[listings["status"] == "Sold"]["listing_id"], 500, replace=True),
    "sale_date": pd.to_datetime([fake.date_between(start_date="-6m", end_date="today") for _ in range(500)]),
    "sale_price": np.random.randint(0.9 * listings["list_price"].min(), 1.1 * listings["list_price"].max(), 500),
    "buyer_name": [fake.name() for _ in range(500)],
    "seller_name": [random.choice(listings["listing_agent"]) for _ in range(500)]
})


# Create relationships between tables using foreign keys
properties = properties.set_index("property_id")
listings = listings.set_index("listing_id")
transactions = transactions.set_index("transaction_id")

# save the dataset to files CSV
path = "C:/Users/OneDrive/Bureau/realstate/"
properties.to_csv(path + "properties.csv")
listings.to_csv(path + "listings.csv")
transactions.to_csv(path + "transactions.csv")
