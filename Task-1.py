def factorial(a):
    if a < 2:
        return 1
    else:
       return a * (factorial(a-1))

n = int(input("enter a number :"))

result = factorial(n)

print("Factorial of",n,"is :",result)

