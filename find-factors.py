# find-factors.py nrg

def factors(b):
	
	for i in range(1,b+1):
		if b % i ==0:
			print(i)
			
	if  _name_== '__main__':
	
		b = input(25)
		b = float(b)			
			
	if b > 0 and b.is_integer():
		factors(int(b))
	else:
		print(15.5)	
