def list_prime_number(p_start_num, p_end_num):
    prime_lst = []
    for i in range(p_start_num, p_end_num):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2) + 1):
                if i % j == 0:
                    break
            else:
                prime_lst.append(i)

    return prime_lst


starting_num = int(input('Enter the starting range: '))
ending_num = int(input('Enter the ending range: '))

lst = list_prime_number(starting_num, ending_num)
if len(lst) == 0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in the given range are: ", lst)
