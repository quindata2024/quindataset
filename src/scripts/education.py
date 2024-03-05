import pandas as pd
import numpy as np
import faker

# Create a Faker instance for realistic data generation
fake = faker.Faker()

# Define parent tables 

students = pd.DataFrame({
    "student_id": [f"ST{str(i).zfill(2)}" for i in range(1, 101)],
    "name": [fake.name() for _ in range(100)],
    "age": np.random.randint(14, 25, 100),
    "grade_level": np.random.choice(["8th", "9th", "10th", "11th", "12th"], 100, replace=True)
})

# Define subjects and corresponding potential course names
courses_by_subject = {
    "Math": ["Statistics", "Algebra", "Geometry", "Calculus", "Number Theory"],
    "Science": ["Biology", "Chemistry", "Physics", "Geology", "Astronomy"],
    "English": ["Literature", "Grammar", "Writing", "Composition", "Poetry"],
    "History": ["World History", "US History", "European History", "Ancient History", "Modern History"]
}

# Generate subjects
subjects = ["Math", "Science", "English", "History"]
repeated_subjects = [subject for subject in subjects for _ in range(5)]

# Generate course names based on subjects
course_names = courses_by_subject["Math"] + courses_by_subject["Science"] + courses_by_subject["English"] + courses_by_subject["History"]

courses = pd.DataFrame({
    "course_id": [f"CS{str(i).zfill(2)}" for i in range(1, 21)],
    "name": course_names,
    "subject": repeated_subjects,
})

# Define child tables linked to parent tables

# Enrollment data
enrollments = pd.DataFrame({
    "student_id": np.random.choice(students["student_id"], 500, replace=True),
    "course_id": np.random.choice(courses["course_id"], 500, replace=True),
    "semester": np.random.choice(["Fall", "Spring"], 500, replace=True)
})

# Grades data (assuming each enrollment has a grade)
grades = pd.DataFrame({
    "enrollment_id": enrollments["student_id"] + enrollments["course_id"],  # Unique identifier
    "student_id": enrollments["student_id"],
    "course_id": enrollments["course_id"],
    "grade": np.random.randint(0, 100, 500)  # % of grading scale
})

# Create relationships between tables using foreign keys
students = students.set_index("student_id")
courses = courses.set_index("course_id")
enrollments = enrollments.set_index(["student_id", "course_id"])
grades = grades.set_index(["student_id", "course_id"])

# save the dataset to files CSV
path = "C:/Users/OneDrive/Bureau/education/"
students.to_csv(path + "students.csv")
courses.to_csv(path + "courses.csv")
enrollments.to_csv(path + "enrollments.csv")
grades.to_csv(path + "grades.csv")
