"""
Project Euler Problem 2
=======================

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will be:

                  1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all the even-valued terms in the sequence which do not
exceed four million.
"""








k = 0
a = 1
b = 2



while k <= 4000000:
    
    if b % 2 == 0:
        k += b

    a ,b = b, a + b
     

print (k)    
