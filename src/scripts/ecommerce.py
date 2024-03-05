import pandas as pd
import numpy as np
from faker import Faker

# Set up Faker for realistic data generation
fake = Faker()

# Define parent tables
customers = pd.DataFrame({
    "customer_id": [f"C{str(i).zfill(2)}" for i in range(1, 101)],
    "name": [fake.name() for _ in range(100)],
    "email": [fake.email() for _ in range(100)],
    "phone_number": [fake.phone_number() for _ in range(100)],
    "address": [fake.address() for _ in range(100)]
})

# Define functions to generate names and descriptions based on category
def generate_name(category):
    if category == "Electronics":
        return f"{np.random.choice(['Smart', 'Portable', 'High-Resolution', 'Wireless', 'AI-Powered'])} {np.random.choice(['TV', 'Headphones', 'Laptop', 'Speaker', 'Drone'])}"
    elif category == "Clothing":
        return f"{np.random.choice(['Stylish', 'Comfortable', 'Casual', 'Formal', 'Activewear'])} {np.random.choice(['T-shirt', 'Jeans', 'Dress', 'Sweater', 'Shoes'])}"
    elif category == "Home":
        return f"{np.random.choice(['Modern', 'Cozy', 'Space-Saving', 'Smart', 'Eco-Friendly'])} {np.random.choice(['Couch', 'Chair', 'Rug', 'Table', 'Storage Container'])}"
    elif category == "Beauty":
        return f"{np.random.choice(['Organic', 'Hydrating', 'Long-Lasting', 'Smoothing', 'Brightening'])} {np.random.choice(['Moisturizer', 'Lipstick', 'Mascara', 'Eyeshadow', 'Serum'])}"
    elif category == "Toys":
        return f"{np.random.choice(['Interactive', 'Educational', 'Creative', 'Plush', 'Action-Packed'])} {np.random.choice(['Robot', 'Doll', 'Puzzle', 'Building Blocks', 'Car'])}"
    else:
        return "Unknown product name"

def generate_description(category):
    if category == "Electronics":
        return f"Experience crystal-clear visuals and immersive sound with our innovative {generate_name(category)}. Perfect for entertainment, work, and everything in between!"
    elif category == "Clothing":
        return f"Look and feel your best in our {generate_name(category)}. Made with high-quality materials for comfort and style that lasts."
    elif category == "Home":
        return f"Transform your space with our {generate_name(category)}. Designed to elevate your home's functionality and aesthetics."
    elif category == "Beauty":
        return f"Achieve a radiant complexion with our {generate_name(category)}. Formulated with nourishing ingredients for visible results."
    elif category == "Toys":
        return f"Spark their imagination and creativity with our {generate_name(category)}. Hours of fun and learning guaranteed!"
    else:
        return "Unknown product description"

# Generate categories
cat = np.random.choice(["Electronics", "Clothing", "Home", "Beauty", "Toys"], 50, replace=True)

# Generate names and descriptions based on categories
names = [generate_name(c) for c in cat]
descriptions = [generate_description(c) for c in cat]


products = pd.DataFrame({
    "product_id": [f"P{str(i).zfill(2)}" for i in range(1, 51)],
    "name": names,
    "category": cat,
    "description": descriptions,
    "price": np.random.randint(10, 1000, 50)
})

# Ensure all column lengths are consistent
customer_ids = [f"C{str(i).zfill(2)}" for i in range(1, 101)]

# Define child tables linked to parent tables
orders = pd.DataFrame({
    "order_id": [f"OR{str(i).zfill(2)}" for i in range(1, 201)],
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
path = "C:/Users/OneDrive/Bureau/ecommerce/"
customers.to_csv(path + "customers.csv")
products.to_csv(path + "products.csv")
orders.to_csv(path + "orders.csv")
order_details.to_csv(path + "order_details.csv")

