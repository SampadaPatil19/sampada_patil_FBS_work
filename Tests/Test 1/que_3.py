# 3. Write a program to accept distance in km and convert it into meters and centimeters both.  

distance = float(input('Enter the distance into Kilometer: '))

# km to m
meter = distance * 1000
print(f'{distance} km is {meter} m into meters.')
print()
# km to cm
centimeter = meter * 100
print(f'{distance} km is {centimeter} cm into centimeters.')