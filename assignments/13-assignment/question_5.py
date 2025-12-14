# 5. Python Program to Sum All the Items in a Dictionary.


# Approach 1
"""def sumItemOfDict(my_dict):

    total = 0

    for value in my_dict.values():
        total += value

    print("Sum of all items:", total)


student_marks = {
    "Maths": 85,
    "Science": 90,
    "English": 78,
    "Computer": 95
}
sumItemOfDict(student_marks)

"""

# Approach 2
def sumDictVal(dict):
    return sum(dict.values())

student_marks = {
    "Maths": 85,
    "Science": 90,
    "English": 78,
    "Computer": 95
}
print(sumDictVal(student_marks))