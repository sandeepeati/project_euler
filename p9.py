#
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


num = [x for x in range(1, 500)]

for a in num:
    for b in num:
        if a < b:
            c = 1000 - (a + b)
            if pow(a, 2) + pow(b, 2) == pow(c, 2):
                print(a, b, c)
                print(a * b * c)
