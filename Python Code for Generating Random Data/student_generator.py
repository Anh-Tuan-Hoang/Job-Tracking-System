import random
from faker import Faker
from helpers import random_float

fake = Faker()

def generate_students(n=1500):
    students = []
    for i in range(1, n + 1):
        students.append({
            "StudentID": i,
            "Name": fake.name(),
            "Email": fake.unique.email(),
            "GPA": random_float(2.0, 4.0),
            "Major": random.choice(["CS", "Biology", "Engineering", "Art", "History"]),
            "DepartmentID": random.randint(1, n),
            "ExpectedGraduationYear": random.randint(2024, 2030),
            "InternshipExperience": random.choice(["Yes", "No"]),
            "Interests": random.choice(["AI", "Healthcare", "Finance", "Education", "Design"]),
            "RecommendationPreference": random.choice(["Opt-In", "Opt-Out", "Custom"])
        })
    return students
