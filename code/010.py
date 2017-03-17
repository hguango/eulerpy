"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


from math import sqrt

def is_prime(m):

    for i in range(3,int(sqrt(m))+1,2):
        if m%i == 0:

	    return False

    return True

#
#
#k = 17 
#
#for i in range(11,2000000,2):
#
#   if is_prime(i):
#
#       k += i
#
#
#
#print k
k=17
i=11
while i<2000000:
 
    if is_prime(i):
        k+=i
    
    i += 2
    
print k