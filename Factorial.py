n = int(input("Enter The Number:"))
factorial = 1
for num in range(n, 1, -1):
    factorial = factorial * num

print(factorial)

def fact(n):
    if n == 1:
        return 1
    else:
        return (n * fact(n - 1))

print(fact(5))
