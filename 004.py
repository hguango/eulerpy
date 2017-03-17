"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def  is_palindromic(m):
    n = m
    sum = 0
    while(m):

        sum = sum * 10 + m % 10
	m = m/10
	
    if 	sum == n:
            
        return  True
    else:
        return False


def is_3digit(m):

    for i in range(999,100,-1):
        if m % i == 0:
	   j = m/i 
	   if  j >=100 and j<= 999:
	       
               return True
    
for i in range(998001,10000,-1):
    ret = is_palindromic(i)

    if ret:
        ret1 = is_3digit(i)

	if ret1:
	    print (i)
	    break
        

