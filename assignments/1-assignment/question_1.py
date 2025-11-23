#1. Write a program to calculate the percentage of student based on marks of any 5 subjects.

sub1 = int(input("Enter marks for Physics:"))
sub2 = int(input("Enter marks for Biology:"))
sub3 = int(input("Enter marks for Chemistry:"))
sub4 = int(input("Enter marks for Math 1:"))
sub5 = int(input("Enter marks for Math 2:"))

total_obtained_marks = sub1+sub2+sub3+sub4+sub5

percentage = total_obtained_marks/500 * 100

print(percentage)

