#
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


from primes import primes_gen

prime_factors = []


def prime_factorization(num):
    for prime in primes_gen(num):
        if num % prime == 0:
            prime_factors.append(prime)
            prime_factorization(num//prime)
            break


prime_factorization(600851475143)


print(max(prime_factors))
