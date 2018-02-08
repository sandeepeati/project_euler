#
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
#  we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?


primes = [2]


def is_prime(num, primes_list):
    """
    checks whether the given number
    is prime or not
    """
    for prime in primes_list:
        if num % prime == 0:
            return False
    return True


# generating primes
# the idea is that every non-prime number is a multiple of any of the primes below it
def primes_gen():
    for i in range(3, 100000000000000, 2):
        if is_prime(i, primes):
            primes.append(i)
            if len(primes) == 10001:
                break


primes_gen()
print(primes[-1])
