# Problem Six
"""

	Author	:	ANOOP P T
	Date	:	02/06/2014
 
	Problem	:	The sum of the squares of the first ten natural numbers is,

	1^2 + 2^2 + ... + 10^2 = 385
	
	The square of the sum of the first ten natural numbers is,

	(1 + 2 + ... + 10)^2 = 55^2 = 3025
	Hence the difference between the sum of the squares of the first ten natural numbers and
	the square of the sum is 3025 - 385 = 2640.

	Find the difference between the sum of the squares of the first one hundred natural numbers and
	the square of the sum.
	
	
"""
import math

sum_of_squares = 0
square_of_sum = 0
for i in range (1,101):
	sum_of_squares = sum_of_squares + i * i
	square_of_sum = square_of_sum + i
square_of_sum = square_of_sum * square_of_sum
difference = int(math.fabs(square_of_sum - sum_of_squares))
print "{x1}-{x2} = {x3}".format(x1=square_of_sum ,x2=sum_of_squares, x3=difference);


#Answer = 25164150