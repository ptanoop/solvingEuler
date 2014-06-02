# Problem Three
"""

	Author	:	ANOOP P T
	Date	:	01/06/2014
 
	Problem	:	The prime factors of 13195 are 5, 7, 13 and 29.

	What is the largest prime factor of the number 600851475143 ?
	
	
"""
import math

def isprime(num):
	is_prime = True;
	sqr = int(math.sqrt(num)) + 1
	for n in range (2, sqr):
		if(num%n==0):
			is_prime = False
			break
	return is_prime


num = 600851475143 
sqr = int(math.sqrt(num) + 1)
largePrimeFactor = 2
for n in range(2,sqr):
	if num % n == 0 and isprime(n):
		largePrimeFactor = n
print largePrimeFactor

# Answer = 6857