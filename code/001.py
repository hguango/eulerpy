"""
Project Euler Problem 1
=======================

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import datetime

k = 0
data = []


t = datetime.datetime.now().microsecond
for i in range(1,1000000,1):
    if i % 3 == 0  or i % 5 ==0 :
        data.append(i)
print (sum(data))

t1 = datetime.datetime.now().microsecond

for i in range(1,1000000,1):
    if i % 3 == 0  or i % 5 ==0 :
        k += i



print k

t2 = datetime.datetime.now().microsecond


print t1-t,t2-t1


