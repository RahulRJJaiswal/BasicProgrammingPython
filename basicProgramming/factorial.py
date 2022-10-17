# Program to calculate factorial using recursion function.

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


n = int(input("Enter number: "))
v_fact = fact(n)
print("Factorial of {0} is: {1}".format(n, v_fact))




