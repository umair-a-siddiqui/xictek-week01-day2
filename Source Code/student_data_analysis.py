# Day 2 Task - Student Data Analysis using Pandas

import pandas as pd

# Step 1: Create student data as a list of dictionaries
students = [
    {"Name": "Umair",  "Age": 20, "Course": "AI/ML",   "Marks": 85},
    {"Name": "Sara",   "Age": 21, "Course": "Web Dev", "Marks": 72},
    {"Name": "Ahmed",  "Age": 22, "Course": "AI/ML",   "Marks": 65},
    {"Name": "Ayesha", "Age": 20, "Course": "MERN",    "Marks": 90},
    {"Name": "Bilal",  "Age": 23, "Course": "AI/ML",   "Marks": 55},
    {"Name": "Hina",   "Age": 21, "Course": "SQA",     "Marks": 78},
    {"Name": "Usman",  "Age": 22, "Course": "Web Dev", "Marks": 60},
    {"Name": "Zara",   "Age": 20, "Course": "AI/ML",   "Marks": 95},
    {"Name": "Hamza",  "Age": 24, "Course": "MERN",    "Marks": 45},
    {"Name": "Fatima", "Age": 21, "Course": "SQA",     "Marks": 88},
]

# Step 2: Convert into a Pandas DataFrame
df = pd.DataFrame(students)

# Step 3: Display all students
print("All Students:")
print(df)

# Step 4: Display students with marks above 70
print("\nStudents with Marks Above 70:")
high_scorers = df[df["Marks"] > 70]
print(high_scorers)

# Step 5: Calculate average marks
average_marks = df["Marks"].mean()
print(f"\nAverage Marks: {average_marks:.2f}")

# Step 6: Find student with highest marks
top_student = df.loc[df["Marks"].idxmax()]
print(f"\nTop Student:\n{top_student}")

# Step 7: Find student with lowest marks
lowest_student = df.loc[df["Marks"].idxmin()]
print(f"\nLowest Scoring Student:\n{lowest_student}")

# Step 8: Total number of students
total_students = len(df)
print(f"\nTotal Number of Students: {total_students}")