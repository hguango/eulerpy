"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""



import math

n = 5
i = 3
while i < 10001:

    is_not = True
    n += 2
    for j in range(3,int(math.sqrt(n)),2):
        if n % j == 0:
            is_not = False
	     
	    break

     
    if is_not:

        i += 1

print (n)
