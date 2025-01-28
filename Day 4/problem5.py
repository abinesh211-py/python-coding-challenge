# Method 1: Using recursion
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Method 2: Using iteration
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Test
num = int(input("Enter the number :"))
print("Factorial (recursive):", factorial_recursive(num))
print("Factorial (iterative):", factorial_iterative(num))
