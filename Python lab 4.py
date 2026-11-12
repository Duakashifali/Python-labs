marks = [85, 90, 78, 88, 95]

total = sum(marks)
average = total / len(marks)

print("Student Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", average)

# task 2
courses = {"Python", "Java", "C++", "Python", "HTML", "Java"}

print("Unique Courses:", courses)

# Task 3
# Student name and roll number in tuple
student = ("Dua", 12345)

# Three subject marks in list
marks = [85, 90, 88]

# Unique skills in set
skills = {"Python", "Java", "HTML", "Python"}

# Student details in dictionary
details = {
    "Program": "BS Software Engineering",
    "Semester": 5
}

# Display student information
print("Student Information")

print("Name:", student[0])
print("Roll Number:", student[1])

print("Subject Marks:", marks)

print("Skills:", skills)

print("Program:", details["Program"])
print("Semester:", details["Semester"])