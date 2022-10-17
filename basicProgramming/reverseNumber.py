# Program to reverse a number in Python

n = int(input("Enter number: "))
reverse_number = 0
while n > 0:
    digit = n % 10
    reverse_number = reverse_number * 10 + digit
    n = int(n / 10)

print('Reverse Number: {0}'.format(reverse_number))
