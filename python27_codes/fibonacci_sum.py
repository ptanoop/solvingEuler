# Problem Two
"""

	Author	:	ANOOP P T
	Date	:	01/06/2014
 
	Problem	:	Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
	By starting with 1 and 2, the first 10 terms will be:

		1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

	By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
	find the sum of the even-valued terms.
	
"""
nth_seq = 1
last_num = 0
fib_sum = 0
while 1 :
	nex_num = nth_seq + last_num
	last_num = nth_seq
	nth_seq  = nex_num
	if nex_num > 4000000 :
		break
	if nex_num % 2 == 0 :
		fib_sum = fib_sum + nex_num
print fib_sum	