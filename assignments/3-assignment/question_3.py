# 3. Write a program to input angles of a triangle and check whether triangle is valid or not.

angle_one = int(input('Enter the first angle: '))
angle_two = int(input('Enter the second angle: '))
angle_three = int(input('Enter the third angle: '))

total_sum_of_angle = angle_one + angle_two + angle_three

if total_sum_of_angle == 180:
    print('Triangle is valid.')
else:
    print('Triangle is Invalid')