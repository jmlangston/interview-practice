# practice from hackerrank python introduction

# raw_input() returns a string without a trailing \n new line
print raw_input()


# arithmetic operators
a = int(raw_input())
b = int(raw_input())
c = int(raw_input())
d = int(raw_input())


print float(a) / b

# yields same results as

from __future__ import division
print a // b


# divmod() is a built-in python function
# it returns a tuple containing (a / b) and the remainder

print divmod(a, b)
# >>> (a/b, a%b)


# pow() is a built-in python function
# given two args, it returns (a ** b)

print pow(a, b)
# pow(2, 3)
# >>> 8

# given three args, it returns (a**b % m)

print pow(a, b, m)
# pow(10, 2, 3)
# >>> 1
