# 1. Write a program to accept year from user and check if it is a leap year or not. 

year = int(input('Enter the year: '))

if year % 4 ==0:
    if year % 100 == 0:
        if year % 400:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is NOT a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is NOT a leap year.")