def fatorar(a):
	dividendo = a
	n = 1
	divisor = 2*n+1
		
	while dividendo>1:
		divisor = (2*n)+1
		if( (dividendo%2) == 0 ):
			print("%5d|%5d" %(dividendo, 2))
			dividendo = dividendo/2
		elif( (dividendo%divisor)==0 ):
			print("%5d|%5d" %(dividendo, divisor))
			dividendo = dividendo/divisor
		else:
			n=n+1
			
	print("%5d| " %(dividendo))



a = int( input("") )
fatorar(a)
		
