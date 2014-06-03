# Problem Ten
"""

	Author	:	ANOOP P T
	Date	:	03/06/2014
 
	Problem	:	The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

						Find the sum of all the primes below two million.

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
	
sum = 2
for i in range(3,2000000,2):
	if isprime(i):
		sum = sum + i
print sum

# Answer = 142913828922