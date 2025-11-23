# 1. Convert the time entered in hh,min and sec into seconds.

hour = int(input('Enter the hours: '))
minutes = int(input('Enter the minutes: '))
seconds = int(input('Enter the seconds: '))

total_seconds =  (hour * 3600) + (minutes * 60) + seconds

print(f"Total seconds of entered time is {total_seconds}.")