def cehckPrime(num):
    v_prime = True
    if num > 1:
        for i in range(2, int(num/2) + 1):
            if (num % i) == 0:
                v_prime = False
                break
    else:
        v_prime = False

    return v_prime


num = int(input("Enter the number to check prime or not: "))
is_prime = cehckPrime(num)
if is_prime:
    print("{0} is a prime number".format(num))
else:
    print("{0} is not a prime number".format(num))
