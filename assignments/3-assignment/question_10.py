#  10. Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18) 

age = int(input('Enter the age of a person: '))

gender = input('Choose your gender, "Male" or "Female": ')

if age >= 21 and (gender == 'Male' or gender == 'male'):
    print(f"You're {age} {gender} and you're eligible for marriage.")

elif age >= 18 and (gender == 'Female' or gender == 'female'):
    print(f"You're {age} {gender} and you're eligible for marriage.")

else:
    print(f"You're {age} {gender} and you're not eligible for marriage.")
    