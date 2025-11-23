"""8. Write a program to prompt user to enter userid and password. After verifying 
userid and password display a 4 digit random number and ask user to enter the 
same. If user enters the same number then show him success message otherwise 
failed. (Something like captcha)"""

import random 

def verifyUser(userId_from_user, password_from_user):
    userId = '#99107'
    password = 'Pass@123'

    if (userId == userId_from_user and password == password_from_user):
        print("Valid credentials.")

        # generate random 4-digit number
        verification_code = random.randint(1000, 9999)

        print(f'Your verification code is {verification_code}')

        # re-enter verfication code
        user_entered = int(input('Re-enter your verification code: '))

        if user_entered == verification_code:
            print('Verification Successful. Congratulations!')

        else:
            print('Verification Failed. Try again.')

    else:
        print('Invalid Credentials. Either userId or password.')
    
userId_from_user = input('Enter Your User Id: ')
password_from_user = input('Enter Your Password: ')

print(verifyUser(userId_from_user, password_from_user))