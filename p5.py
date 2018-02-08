#
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
# without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# the solution is to find the lcm of the first 20 numbers
# lcm of 2 numbers = product of 2 numbers / gcd of 2 numbers


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


def lcm_of_list(num_list):
    _lcm = lcm(num_list[0], num_list[1])
    for i in range(2, len(num_list)):
        _lcm = _lcm(_lcm, num_list[i])
    return _lcm


print(lcm_of_list([x for x in range(2, 21)]))
