import pandas as pd
import numpy as np
from faker import Faker

# Set up Faker for realistic data generation
fake = Faker()

# Employees (including basic information and hire date)
employees = pd.DataFrame({
    "employee_id": [f"E{str(i).zfill(3)}" for i in range(1, 1001)],
    "first_name": [fake.first_name() for _ in range(1000)],
    "last_name": [fake.last_name() for _ in range(1000)],
    "email": [fake.email() for _ in range(1000)],
    "job_title": [fake.job() for _ in range(1000)],
    "hire_date": pd.to_datetime([fake.date_between(start_date="-5y", end_date="today") for _ in range(1000)]),
    "address": [fake.address() for _ in range(1000)],
    "phone_number": [fake.phone_number() for _ in range(1000)]
})

# Departments (including location and manager)
departments = pd.DataFrame({
    "department_id": [f"D{str(i).zfill(2)}" for i in range(1, 21)],
    "name": ["Marketing", "Sales", "Finance", "HR", "IT", "Engineering", "Customer Service", "Legal", "Product", "Operations",
             "Research & Development", "Accounting", "Administration", "Executive", "Quality Assurance", "Security", "Facilities",
             "Training", "Finance", "Transversal"],  # 20 names
    "location": [fake.city() for _ in range(20)],
    "manager_id": np.random.choice(employees["employee_id"], 20, replace=True)  # Assign managers randomly
})

# Salaries (including current salary and start date)
salaries = pd.DataFrame({
    "salary_id": [f"S{str(i).zfill(3)}" for i in range(1, 1001)],
    "employee_id": np.random.choice(employees["employee_id"], 1000, replace=True),
    "start_date": pd.to_datetime([fake.date_between(start_date="-3y", end_date="today") for _ in range(1000)]),
    "current_salary": np.random.randint(30000, 200000, 1000)
})

# Benefits (including health insurance plan and enrollment status)
benefits = pd.DataFrame({
    "benefit_id": [f"B{str(i).zfill(3)}" for i in range(1, 1001)],
    "employee_id": np.random.choice(employees["employee_id"], 1000, replace=True),
    "health_plan": np.random.choice(["PPO", "HMO", "HSA"], 1000, replace=True),
    "enrolled": np.random.choice([True, False], 1000, replace=True)
})


# Create relationships between tables using foreign keys
employees = employees.set_index("employee_id")
departments = departments.set_index("department_id")
salaries = salaries.set_index("salary_id")
benefits = benefits.set_index("benefit_id")

# save the dataset to files CSV
path = "C:/Users/OneDrive/Bureau/humanressource/"
employees.to_csv(path + "employees.csv")
departments.to_csv(path + "departments.csv")
salaries.to_csv(path + "salaries.csv")
benefits.to_csv(path + "benefits.csv")
