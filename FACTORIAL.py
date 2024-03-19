def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
number = int(input("Enter a number to find its factorial: "))
factorial_iter = factorial_iterative(number)
print(f"Factorial of {number} (iterative): {factorial_iter}")
factorial_rec = factorial_recursive(number)
print(f"Factorial of {number} (recursive): {factorial_rec}")