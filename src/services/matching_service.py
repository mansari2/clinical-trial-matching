class MatchingService:
    def __init__(self, trial_database):
        self.trial_database = trial_database

    def match_patient_to_trial(self, patient_data):
        # Analyze patient data and match to relevant clinical trials
        matched_trials = []
        for trial in self.trial_database:
            if self.is_eligible(patient_data, trial):
                matched_trials.append(trial)
        return matched_trials

    def is_eligible(self, patient_data, trial):
        # Check eligibility criteria
        eligibility_criteria = trial.get('eligibility_criteria', {})
        for criterion, value in eligibility_criteria.items():
            if patient_data.get(criterion) != value:
                return False
        return True