# 4. Write a program to input all sides of a triangle and check whether triangle is valid or not.

side1 = int(input('Enter the positive length of side1: '))
side2 = int(input('Enter the positive length of side2: '))
side3 = int(input('Enter the positive length of side3: '))

"""
Triangle is consider as valid 
when the sum of lengths of any two sides of triangle is 
greater than lenght os third side
"""

if (side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2):
    print('Triangle is Valid.')
else:
    print('Triangle is Invalid.')