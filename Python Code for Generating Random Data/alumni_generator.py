import random
from faker import Faker

fake = Faker()

def generate_alumni(n=1500):
    alumni = []
    for i in range(1, n + 1):
        alumni.append({
            "AlumniID": i,
            "Name": fake.name(),
            "Email": fake.unique.email(),
            "GradYear": random.randint(1990, 2023),
            "CurrentPosition": fake.job(),
            "YearsOfExperience": random.randint(1, 30),
            "InterestedInShortTerm": random.choice(["Yes", "No"]),
            "DepartmentID": random.randint(1, n)
        })
    return alumni
