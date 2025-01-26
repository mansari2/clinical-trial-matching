from typing import TypedDict, List

class Patient(TypedDict):
    id: str
    name: str
    age: int
    medical_history: List[str]
    eligibility_criteria: dict

class Trial(TypedDict):
    id: str
    title: str
    description: str
    eligibility_criteria: dict
    location: str
    start_date: str
    end_date: str