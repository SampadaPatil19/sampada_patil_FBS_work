# 9. Input 5 subject marks from user and display grade(eg.First class,Second class ..) 

sub1 = float(input('Enter the mark of subject 1: '))
sub2 = float(input('Enter the mark of subject 2: '))
sub3 = float(input('Enter the mark of subject 3: '))
sub4 = float(input('Enter the mark of subject 4: '))
sub5 = float(input('Enter the mark of subject 5: '))

total_score = sub1 + sub2 + sub3 + sub4 + sub5

percentage = total_score / 500 * 100

if percentage > 90:
    print('Grade is first class.')

elif percentage >= 80:
    print('Grade is second class.')

elif percentage >= 70:
    print('Grade is third class.')
    
else:
    print('Grade is fourth class.')
    