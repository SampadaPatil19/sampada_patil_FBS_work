"""
Write a program to prompt user to enter userid and password. If Id and  
password is incorrect give him chance to re-enter the credentials. Let him try 3  
times. After that program to terminate. 
"""

count = 3

user_id = '#123gunjan'
password = 'Pass@123'

while count > 0:
    user_entered_id = input('Enter your user id: ')
    user_entered_password = input('Enter your Password: ')

    if user_entered_id == user_id and user_entered_password == password:
        print('Login Successful. Congratulations!')
        break
    else:
        count -= 1
        if count > 0:
            print(f'Incorrect credentials. You have {count} attempts left. Re-enter your Credentials.')
        else:
            print('Incorrect credentials. You have exceeded the maximum number of attempts. Program will terminate.')
