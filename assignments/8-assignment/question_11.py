# WAP to check if a given number is Armstrong number or not. For each task create separate functions.

def armstrongNum(num, total_dig):
    if num == 0:
        return 0
    
    else:
        sum = 0
        while num > 0:
            last_dig = num % 10 
            sum = sum + last_dig**total_dig
            num = num // 10

    return sum

def checkArmStrongNum(num, total_dig):
    if armstrongNum(num, total_dig) == num:
        return f'{num} is ArmStrong Number.'
    
    else:
        return f'{num} is not ArmStrong Number.'
    
print(checkArmStrongNum(154, 3))