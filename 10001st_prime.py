# Problem Seven
"""

	Author	:	ANOOP P T
	Date	:	02/06/2014
 
	Problem	:	By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

	What is the 10001st prime number?
	
	
"""

import math
import time

def isprime(num):
	is_prime = True;
	sqr = int(math.sqrt(num)) + 1
	for n in range (2, sqr):
		if(num%n==0):
			is_prime = False
			break
	return is_prime

c  = time.time()
is10001prime = False
num = 1
primepos = 0
while not is10001prime:
	num+=1
	if isprime(num):
		primepos+=1
	if primepos==10001:
		is10001prime = True
print "10001st prime = {x} ".format(x=num)
print time.time()-c

# Answer = 104743
