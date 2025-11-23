# 3. Convert distant given in feet and inches into meter and centimeter.

feet = float(input('Enter the distance in Feet: '))
inches = float(input('Enter the distance in Inches: '))

total_inches = feet * 12 + inches

# Converting into cm
centimeter = total_inches * 2.54

# Converting into m
meters = centimeter / 100

print(f'Total centimeter of given distance is {centimeter}')
print(f'Total meters of given distance is {meters}')