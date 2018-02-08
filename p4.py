#
#
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(s):
    return str(s) == str(s)[::-1]

palindromes = []
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        p = i * j
        if is_palindrome(p):
            palindromes.append(p)

print(max(palindromes))
