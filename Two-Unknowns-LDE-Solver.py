def gcd(a,b):
	r1 = abs(a)
	r2 = abs(b)
	x1 = 1
	y1 = 0
	x2 = 0
	y2 = 1
	r = q = x = y  = 0
	print("%5d %5s %5d %5d" %(r1, "*", x1, y1))
	print("%5d %5s %5d %5d" %(r2, "*", x2, y2))
	q = r1//r2
	r = r1%r2
	x = -q*x2+x1;
	y = -q*y2+y1;
	
	x1 = x2
	y1 = y2
	x2 = x
	y2 = y
	
	r1 = r2
	r2 = r
	
	while( r2!=0 ):
		print("%5d %5d %5d %5d" %(r, q, x, y))
		q = r1//r2
		r = r1%r2
		x = (-q)*x2 + x1;
		y = (-q)*y2 + y1;
		
		x1 = x2
		y1 = y2
		x2 = x
		y2 = y
		
		r1 = r2
		r2 = r

	print("%5d %5c %5c %5c" %(r2, '-', '-', '-'))
	return r1, x1, y1

a = int( input("a: ") )
b = int( input("b: ") )
n = int( input("n: ") )
print("============ Extended Euclidean algorithm ============")
gcd, x , y = gcd(a,b)

if( a<0):
	x = x*(-1)
if( b<0):
	y = y*(-1)
print("(%d).X + (%d).Y = %d"%(a, b, n))	
print( "gcd(%d,%d)=%d" %(a, b, gcd))
print("gcd(%d,%d) = (%d).(%d) + (%d).(%d)" %(a,b,x,a,y,b) )
print("%d = (%d).(%d) + (%d).(%d)" %(gcd,x,a,y,b) )
print("=====================================================")
if( not((n%gcd) == 0) ):
	print("the equation don't have integer solution")
else:
	print("the equation have integer solution")
	print("give a valid particular solution")
	x0 = int( input("X0: ") )
	y0 = int( input("Y0: ") )
	print("Then:")
	print("X = %d + (%d).t" % (x0, (b/gcd)))
	print("Y = %d - (%d).t" % (y0, (a/gcd)))