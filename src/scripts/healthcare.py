import pandas as pd
import numpy as np
import faker
import random

# Create a Faker instance for generating realistic data
fake = faker.Faker()

# Define parent tables
patients = pd.DataFrame({
    "patient_id": [f"P{str(i).zfill(2)}" for i in range(1, 101)],
    "name": [fake.name() for _ in range(100)],
    "address": [fake.address() for _ in range(100)],
    "phone_number": [fake.phone_number() for _ in range(100)],
    "email": [fake.email() for _ in range(100)],
    "birth_date": pd.to_datetime([fake.date_of_birth() for _ in range(100)])
})

## Generate diagnosis codes and descriptions

descriptions = [
                "Common cold", "Influenza (flu)", "Asthma", "Diabetes",
                "Hypertension", "Bronchitis", "Pneumonia", "Allergies",
                "Arthritis", "Osteoporosis", "Migraine", "Anxiety disorder",
                "Depression", "Gastroenteritis", "Urinary tract infection (UTI)", "Sinusitis",
                "Conjunctivitis (pink eye)", "Gastritis", "Acid reflux", "Peptic ulcer",
                "Eczema", "Psoriasis", "Gout", "Fibromyalgia",
                "Chronic obstructive pulmonary disease (COPD)", "Emphysema", "Anemia", "Hyperthyroidism",
                "Hypothyroidism", "Irritable bowel syndrome (IBS)", "Crohn's disease", "Ulcerative colitis",
                "Hepatitis", "Cirrhosis", "Diverticulitis", "Diverticulosis",
                "Stroke", "Heart attack", "Atrial fibrillation", "Angina",
                "Chronic kidney disease", "Urinary incontinence", "Glaucoma", "Cataracts",
                "Macular degeneration", "Menopause", "Erectile dysfunction", "Premenstrual syndrome (PMS)",
                "Endometriosis", "Polycystic ovary syndrome (PCOS)"]

diagnoses_codes = []
for _ in range(50):
    diagnosis_code = "DC" + str(random.randint(100, 999)).zfill(3)
    diagnoses_codes.append(diagnosis_code)

diagnoses = pd.DataFrame({
    "diagnosis_id": [f"D{str(i).zfill(2)}" for i in range(1, 51)],
    "diagnosis_code": diagnoses_codes,
    "description": descriptions
})

## Define child tables linked to parent tables
# Common medications
common_medications = [ "Aspirin", "Ibuprofen", "Acetaminophen", "Lisinopril", "Simvastatin",
                        "Metformin", "Levothyroxine", "Losartan", "Amlodipine", "Atorvastatin",
                        "Albuterol", "Furosemide", "Omeprazole", "Gabapentin", "Hydrochlorothiazide",
                        "Metoprolol", "Metformin", "Escitalopram", "Sertraline", "Citalopram",
                        "Doxycycline", "Amoxicillin", "Azithromycin", "Cephalexin", "Prednisone",
                        "Warfarin", "Diazepam", "Fluoxetine", "Lorazepam", "Clonazepam",
                        "Hydrocodone", "Oxycodone", "Tramadol", "Codeine", "Morphine",
                        "Fentanyl", "Buprenorphine", "Methadone", "Naloxone", "Benzonatate",
                        "Cetirizine", "Loratadine", "Fexofenadine", "Diphenhydramine", "Promethazine",
                        "Ondansetron", "Prochlorperazine", "Metoclopramide", "Docusate", "Senna",
                        "Omeprazole", "Esomeprazole", "Ranitidine", "Famotidine", "Pantoprazole",
                        "Alendronate", "Risedronate", "Ibandronate", "Ezetimibe", "Rosuvastatin",
                        "Pravastatin", "Fluvastatin", "Lovastatin", "Prazosin", "Doxazosin",
                        "Terazosin", "Tamsulosin", "Finasteride", "Dutasteride", "Sildenafil",
                        "Tadalafil", "Vardenafil", "Finasteride", "Dutasteride", "Minoxidil",
                        "Tretinoin", "Isotretinoin", "Adapalene", "Clindamycin", "Benzoyl peroxide",
                        "Hydrocortisone", "Triamcinolone", "Fluticasone", "Mometasone", "Prednisolone",
                        "Estradiol", "Conjugated estrogens", "Levonorgestrel", "Norethindrone", "Drospirenone"]
# Generate medications
medications = [("M" + str(i).zfill(3), random.choice(common_medications)) for i in range(1, 201)]

# Generate instructions
instructions = ["Take as directed or call the doctor for more info." for _ in range(200)]

prescriptions = pd.DataFrame({
    "prescription_id": [f"PR{str(i).zfill(2)}" for i in range(1, 201)],
    "patient_id": np.random.choice(patients["patient_id"], 200, replace=True),
    "medication": medications,
    "dosage": [fake.pyint() for _ in range(200)],
    "instructions": instructions,
})

# Generate procedures and providers
providers = ["Dr. " + fake.name() for _ in range(150)]
procedures_list = [
    "Physical therapy","Surgery","Medication management","Counseling", "Diagnostic imaging",
    "Laboratory tests","Rehabilitation","Chiropractic adjustment", "Massage therapy","Acupuncture",
    "Occupational therapy","Speech therapy","Electroconvulsive therapy",
    "Radiation therapy","Chemotherapy","Dialysis","Cardiac catheterization","Endoscopy",
    "Colonoscopy","Lumbar puncture","Biopsy","Joint injection","Dental extraction","Root canal",
    "Eye surgery","Plastic surgery","Laser therapy","Blood transfusion","Bone marrow transplant",
    "Appendectomy","Hernia repair","Cesarean section","Vasectomy","Tonsillectomy",
    "Appendectomy","Hysterectomy","Arthroscopy","Angioplasty","Coronary bypass",
    "Kidney transplant","Liver transplant","Lung transplant",
    "Orthopedic surgery","Neurosurgery","Urological surgery","Bariatric surgery",
    "Cataract surgery","Cosmetic surgery","Orthodontic treatment", "general Dialysis"]
procedures = procedures_list + ["follow " + procedure for procedure in procedures_list] \
    + ["step of " + procedure for procedure in procedures_list]

treatments = pd.DataFrame({
    "treatment_id": [f"T{str(i).zfill(2)}" for i in range(1, 151)],
    "patient_id": np.random.choice(patients["patient_id"], 150, replace=True),
    "diagnosis_id": np.random.choice(diagnoses["diagnosis_id"], 150, replace=True),
    "procedure": procedures,
    "provider": providers,
    "date": pd.to_datetime([fake.date_between(start_date="-1y", end_date="today") for _ in range(150)])
})

# Create relationships between tables using foreign keys
patients = patients.set_index("patient_id")
diagnoses = diagnoses.set_index("diagnosis_id")
prescriptions = prescriptions.set_index(["patient_id", "prescription_id"])
treatments = treatments.set_index(["patient_id", "treatment_id", "diagnosis_id"])

#  Save datasets to CSV
path = "C:/Users/OneDrive/Bureau/healthcare/"
patients.to_csv(path + "patients.csv")
diagnoses.to_csv(path + "diagnoses.csv")
prescriptions.to_csv(path + "prescriptions.csv")
treatments.to_csv(path + "treatments.csv")
