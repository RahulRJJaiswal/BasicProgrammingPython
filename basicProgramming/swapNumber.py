def swapNumber(p_num1, p_num2):
    temp = p_num1
    p_num1 = p_num2
    p_num2 = temp

    return p_num1, p_num2


num1 = int(input("Enter the 1st number:"))
num2 = int(input("Enter the 2nd number:"))

# Printing the numbers before swap
print('The value of num1 before swapping: {}'.format(num1))
print('The value of num2 before swapping: {}'.format(num2))

num1, num2 = swapNumber(num1, num2)

# Printing the numbers after swap
print('The value of num1 after swapping: {}'.format(num1))
print('The value of num2 after swapping: {}'.format(num2))
