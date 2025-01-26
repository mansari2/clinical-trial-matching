class Patient:
    def __init__(self, patient_id, name, age, medical_history):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.medical_history = medical_history

class ClinicalTrial:
    def __init__(self, trial_id, title, eligibility_criteria):
        self.trial_id = trial_id
        self.title = title
        self.eligibility_criteria = eligibility_criteria

__all__ = ['Patient', 'ClinicalTrial']