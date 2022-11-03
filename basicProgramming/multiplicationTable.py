def display_table(num):
    for i in range(1, 11):
        print("{0} x {1} = {2}".format(i, num, i * num))


num = int(input("Enter the number: "))
print("The Multiplication Table of: ", num)
display_table(num)
