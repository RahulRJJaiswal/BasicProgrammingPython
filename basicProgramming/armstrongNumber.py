"""
The armstrong number can be defined as n-digit numbers
equal to the sum of the nth powers of their digits are called armstrong numbers.

Ex: 153 here number of digit is 3

153 = 1^3 + 5^3 + 3^3
153 = 1 + 125 + 9
"""


def get_sum_of_nth_powers(p_num):
    v_num_digit = len(str(p_num))
    total = 0

    while p_num > 0:
        v_digit = p_num % 10
        total = total + (v_digit ** v_num_digit)
        p_num = p_num // 10  # int(p_num / 10) it is also same

    return total


def is_armstrong(p_num):
    if p_num == get_sum_of_nth_powers(p_num):
        print("{0} is a armstrong number".format(p_num))
    else:
        print("{0} is not a armstrong number".format(p_num))


num = int(input("Enter the number: "))
is_armstrong(num)

