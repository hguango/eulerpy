"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


n = 600851475143



i = 3

while i < n/2:

    if n % i == 0:
        n = n/i

    i +=2 





#for i in range(3,n/2+1,2):
#
 #   if n % i == 0:
  #      n = n/i

	
        

print (n)

