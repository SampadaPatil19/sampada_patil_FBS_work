# 8. Write a program to convert days into years, weeks and days.

def convertIntoDays(total_days):
    days_in_weeks = 7

    # number of years
    years = total_days // 365
    remaining_days = total_days % 365

    # number of weeks
    weeks = remaining_days // days_in_weeks
    
    # number of days
    days = remaining_days % days_in_weeks

    return years, weeks, days


total_days = int(input('Enter the number of days: '))
years, weeks, days = convertIntoDays(total_days)
print(f'Years are {years}.\nWeeks are {weeks}.\nDays are {days}.')