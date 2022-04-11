from math import sqrt

def possible_dividers(x):
	primos = []
	primo = 2
	n = 1
	while primo < int(sqrt(x)):
		primos.append(primo)
		primo = 2*n+1
		n = n+1
	return primos
		

flag = 1
a = int( input("a: ") )

print("raiz de %d: %f"%(a, sqrt(a)))

P = possible_dividers(a)

print("P = { ", end="")
for p in P:
	print("%d, "%(p), end="" )
print("}")

quantidade_de_divisores = 0
for p in P:
	print("(%d / %d) , Q = %d, R=%d" %(a, p, a/p, a%p))

if(flag):
	print("%d is prime" %(a))
else:
	print("%d is not prime" %(a))

for p in P:
	if( (a%p) == 0 ):
		flag = 0
		print("is multiple of %d"%(p))
		break
