# Problem Five
"""

	Author	:	ANOOP P T
	Date	:	02/06/2014
 
	Problem	:	2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

	What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
	
	Some Logic Info
		Divisible 20 means divisible by 1(ofcourse), 2, 4, 5, 10
		Divisible 18 means divisible by 3, 6, 9
		Divisible 16 means divisible by 8
		Divisible 14 means divisible by 7
		So only we want to check number is divisible by 11 - 20 
	
	
"""
num = 0
loop_live = True
while (loop_live):
	num = num + 20
	isrem = False
	for i in range(19,10,-1):
		if(num%i!=0):
			isrem = True
			break
	if(isrem==False):
		loop_live = False
print num		

# Answer = 232792560