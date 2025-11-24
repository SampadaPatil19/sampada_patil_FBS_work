"""
Enter number of students from user. For those many students accept marks of 5  
subject marks from user and calculate percentage. Display all percentage and  
average percentage of students.
"""


# Take number of students
num_students = int(input("Enter number of students: "))

# To store total percentages
total_percentage = 0

for s in range(num_students):
    print("\nEnter marks of 5 subjects for student", s + 1)

    # Take 5 subject marks
    sub1 = float(input("Subject 1: "))
    sub2 = float(input("Subject 2: "))
    sub3 = float(input("Subject 3: "))
    sub4 = float(input("Subject 4: "))
    sub5 = float(input("Subject 5: "))

    # Calculate total marks of 5 subjects
    total = sub1 + sub2 + sub3 + sub4 + sub5

    # Calculate percentage
    percentage = (total / 500) * 100
    print("Percentage of student", s + 1, "=", percentage, "%")

    # Keep adding to calculate average later
    total_percentage += percentage

# Calculate average percentage of all students
avg = total_percentage / num_students

print("\nAverage percentage of all students =", avg, "%")
