# primes is a list with 2 already added
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
def primes_gen(n):
    yield 2
    for i in range(3, n + 1, 2):
        if is_prime(i, primes):
            primes.append(i)
            yield i
