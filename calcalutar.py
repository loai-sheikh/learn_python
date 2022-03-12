def factorial(val):
    return 1 if (val < 1) else val * factorial(val - 1)

print(factorial(4))

