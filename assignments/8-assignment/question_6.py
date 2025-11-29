def fibonacci_series(n):
    if n <= 0:
        print("Number of terms should be positive.")
        return
    a, b = 1, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

n = int(input("Enter the number of terms: "))
fibonacci_series(n)


