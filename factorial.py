# Complete the factorial function below.
def factorial(n):
    if n == 1:
        return 1
    elif n <= 0:
        return 'Value Error'
    else:
        return (n * factorial(n-1))

print(factorial(5))
