def gcd(a,b):
	a = abs(a)
	b = abs(b)

	while( b!=0):
		resto = a%b
		a = b
		b = resto

	return a

a = int( input("a: ") )
b = int( input("b: ") )
print("gcd(%d, %d) = %d" % (a, b, gcd(a, b) ) )
