import pandas as pd
import numpy as np
import faker

# Create a Faker instance for generating realistic data
fake = faker.Faker()

# Define parent tables
patients = pd.DataFrame({
    "patient_id": np.arange(100),  # Unique identifier
    "name": [fake.name() for _ in range(100)],
    "address": [fake.address() for _ in range(100)],
    "phone_number": [fake.phone_number() for _ in range(100)],
    "email": [fake.email() for _ in range(100)],
    "birth_date": pd.to_datetime([fake.date_of_birth() for _ in range(100)])
})

diagnoses = pd.DataFrame({
    "diagnosis_id": np.arange(50),
    "diagnosis_code": [fake.word() for _ in range(50)],
    "description": [fake.sentence() for _ in range(50)]
})

# Define child tables linked to parent tables
prescriptions = pd.DataFrame({
    "prescription_id": np.arange(200),
    "patient_id": np.random.choice(patients["patient_id"], 200, replace=True),
    "medication": [fake.word() for _ in range(200)],
    "dosage": [fake.pyint() for _ in range(200)],
    "instructions": [fake.sentence() for _ in range(200)]
})

treatments = pd.DataFrame({
    "treatment_id": np.arange(150),
    "patient_id": np.random.choice(patients["patient_id"], 150, replace=True),
    "diagnosis_id": np.random.choice(diagnoses["diagnosis_id"], 150, replace=True),
    "procedure": [fake.word() for _ in range(150)],
    "provider": [fake.name() for _ in range(150)],
    "date": pd.to_datetime([fake.date_between(start_date="-1y", end_date="today") for _ in range(150)])
})

# Create relationships between tables using foreign keys
patients = patients.set_index("patient_id")
diagnoses = diagnoses.set_index("diagnosis_id")
prescriptions = prescriptions.set_index(["patient_id", "prescription_id"])
treatments = treatments.set_index(["patient_id", "treatment_id", "diagnosis_id"])

#  Save datasets to CSV
path = "C:/Users/quindata/OneDrive/Bureau/healthcare/"
patients.to_csv(path + "patients.csv")
diagnoses.to_csv(path + "diagnoses.csv")
prescriptions.to_csv(path + "prescriptions.csv")
treatments.to_csv(path + "treatments.csv")
