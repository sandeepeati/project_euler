#
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.


from primes import primes_gen

sum_below_2million = 0

for i in primes_gen(2000000):
    sum_below_2million += i

print(sum_below_2million)
