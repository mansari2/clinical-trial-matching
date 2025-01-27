import json
import random
from faker import Faker

# Simple script to generate mock EHR data
fake = Faker()

# Generate mock patient data
def generate_patient_data(num_patients=10):
    patients = []
    for _ in range(num_patients):
        patient = {
            "patient_id": fake.uuid4(),
            "name": fake.name(),
            "age": random.randint(18, 85),
            "gender": random.choice(["Male", "Female", "Other"]),
            "medical_conditions": random.sample(
                [
                    "diabetes",
                    "hypertension",
                    "asthma",
                    "cancer",
                    "heart disease",
                    "obesity",
                    "depression",
                    "anxiety",
                    "arthritis",
                    "COVID-19",
                    "chronic kidney disease",
                    "stroke",
                    "COPD",
                    "migraine",
                    "osteoporosis",
                    "epilepsy",
                    "HIV/AIDS",
                    "hepatitis",
                    "multiple sclerosis",
                ],
                random.randint(1, 3),
            ),
            "medications": random.sample(
                [
                    "metformin",
                    "lisinopril",
                    "albuterol",
                    "insulin",
                    "atorvastatin",
                    "omeprazole",
                    "sertraline",
                    "amlodipine",
                    "levothyroxine",
                    "losartan",
                    "gabapentin",
                    "hydrochlorothiazide",
                    "furosemide",
                    "prednisone",
                    "clopidogrel",
                    "warfarin",
                    "amoxicillin",
                    "azithromycin",
                ],
                random.randint(1, 2),
            ),
            "lab_results": {
                "A1C": round(random.uniform(4.5, 12.0), 1),  # Diabetes indicator
                "BP_sys": random.randint(90, 180),  # Blood pressure systolic
                "BP_dia": random.randint(60, 120),  # Blood pressure diastolic
                "cholesterol": round(random.uniform(150, 300), 1),
                "heart_rate": random.randint(60, 100),
            },
            "location": fake.city(),
            "insurance": random.choice(["Private", "Medicare", "Medicaid", "Uninsured"]),
        }
        patients.append(patient)
    return patients


# Save the mock data to a JSON file
def save_to_json(data, filename="mock_ehr_data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Mock EHR data saved to {filename}")


if __name__ == "__main__":
    num_patients = 20  # Change this number as needed
    patients = generate_patient_data(num_patients)
    save_to_json(patients)
