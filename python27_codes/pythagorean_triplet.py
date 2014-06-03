# Problem Nine
"""

	Author	:	ANOOP P T
	Date	:	03/06/2014
 
	Problem	:	A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

						a^2 + b^2 = c^2
						For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

						There exists exactly one Pythagorean triplet for which a + b + c = 1000.
						Find the product abc.

"""

got = False
s = 1000
for a in range(3, s-3):
	for b in range(a + 1,s - 4):
		c = s - (a + b)
		if c*c == a*a + b*b:
			print a*b*c
			
# Answer = 31875000 ( 200^2 + 375^2 = 425^2 ) ( 200 + 375 + 425 = 1000 )