# Problem Four
"""

	Author	:	ANOOP P T
	Date	:	02/06/2014
 
	Problem	:	A palindromic number reads the same both ways.
	The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

	Find the largest palindrome made from the product of two 3-digit numbers.
	
	
"""

# python module to check palindrome or not
def isPalindrome(num):
	rev = 0
	tmp = num
	while(tmp>0):
		n = tmp % 10
		rev = rev * 10 + n
		tmp = int(tmp/10)
	if(rev==num):
		return True
	else:
		return False

		
x1 = 0
x2 = 0
large_mul = 0
for n in range(999,100,-1):
	for i in range(n-1,100,-1):
		mul = n * i
		if(isPalindrome(mul)):			
			if(large_mul<mul):
				x1 = n
				x2 = i
				large_mul = mul			
			break
print "{x1} x {x2} = {x3}".format(x1=x1, x2=x2,x3 = large_mul)
	