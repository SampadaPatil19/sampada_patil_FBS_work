# 5. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.


side1 = float(input("Enter length of side 1: "))
side2 = float(input("Enter length of side 2: "))
side3 = float(input("Enter length of side 3: "))

if side1 == side2 == side3:
    print("The triangle is EQUILATERAL.")

elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is ISOSCELES.")

else:
    print("The triangle is SCALENE.")
