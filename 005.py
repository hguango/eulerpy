"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""

m,n = 3,2

def smallest(m,n):
    a, b = m,n
    while n != 0:
        m, n = n, m % n
            
    return a*b/m

while n < 20:
        
    m,n = smallest(m,n),n+1       


print (m)

#print (232792560)

