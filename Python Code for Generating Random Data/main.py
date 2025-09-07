from student_generator import generate_students
from alumni_generator import generate_alumni
from department_generator import generate_departments
from job_generator import generate_jobs
from recruiter_generator import generate_recruiters
from company_generator import generate_companies
from staff_generator import generate_university_staff
from save_utils import save_to_csv

# Output folder
BASE_PATH = "C:/Users/ANH TUAN/Desktop/3400H/proj/fakedata/"

def main():
    students = generate_students()
    alumni = generate_alumni()
    departments = generate_departments()
    jobs = generate_jobs()
    recruiters = generate_recruiters()
    companies = generate_companies()
    staff = generate_university_staff()

    save_to_csv(students, BASE_PATH + "students.csv")
    save_to_csv(alumni, BASE_PATH + "alumni.csv")
    save_to_csv(departments, BASE_PATH + "departments.csv")
    save_to_csv(jobs, BASE_PATH + "jobs.csv")
    save_to_csv(recruiters, BASE_PATH + "recruiters.csv")
    save_to_csv(companies, BASE_PATH + "companies.csv")
    save_to_csv(staff, BASE_PATH + "universitystaff.csv")

    print("Data generation complete. Files saved.")

if __name__ == "__main__":
    main()
