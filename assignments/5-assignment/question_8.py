# Write a program to solve the following series :

# a. 1! + 2! + 3! + ... + n!

n = int(input("Enter n for factorial sum (1! + 2! + ... + n!): "))
factorial_sum = 0

for i in range(1, n+1):
    factorial = 1
    for j in range(1, i+1):
        factorial *= j
    factorial_sum += factorial

print(f"Sum of factorial series: {factorial_sum}")

# b. N + N^2 + N^3 + ... + N^N

N = int(input("Enter N for power series (N + N^2 + ... + N^N): "))
power_sum = 0
for i in range(1, N+1):
    power_sum += N ** i
print(f"Sum of power series: {power_sum}")

# c. Find the sum of geometric series from 1 to n where the common ratio is 2.

n_geo = int(input("Enter n for geometric series (common ratio 2): "))
# Sum of geometric series with first term 1 and ratio 2: 1 + 2 + 4 + ... + 2^(n_geo-1)
geom_sum = 0
term = 1
for i in range(n_geo):
    geom_sum += term
    term *= 2
print(f"Sum of geometric series: {geom_sum}")

# d. S = a + a^2/2 + a^3/3 + ... + a^10/10

a = float(input("Enter a for series d (a + a^2/2 + ... + a^10/10): "))
series_d_sum = 0
for i in range(1, 11):
    series_d_sum += (a ** i) / i
print(f"Sum of series d: {series_d_sum}")

# e. S = x - x^2/3 + x^3/5 - x^4/7 + ... to n terms

x = float(input("Enter x for series e: "))
n_terms = int(input("Enter number of terms for series e: "))
series_e_sum = 0

for i in range(1, n_terms + 1):
    term = (x ** i) / (2 * i - 1)
    if i % 2 == 0:
        series_e_sum -= term
    else:
        series_e_sum += term

print(f"Sum of series e: {series_e_sum}")
