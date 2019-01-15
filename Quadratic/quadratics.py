# quadratics.py nrg

def roots(a,b,c):
	D = (b*b - 4*a*c)**.5
	x_1 = (-b + D) / (2 *a)
	x_2 = (-b - D) / (2 *a)
	print('x1: {0}'.format(x_1))
	print('x2: {0}'.format(x_2))
	
  if  _name_== '__main__':
	a = input ('Enter a: ')
	b = input ('Enter b: ')
	c = input ('Enter c: ')
	roots(float(a), float(b), float(c))
	
'''
console
nrg@dmz:~/python$ python3 quadratics.py
Enter a: 1
Enter b: 0
Enter c: -9
x1: 3.0
x2: -3.0
nrg@dmz:~/python$ python3 quadratics.py
Enter a: 1
Enter b: 0
Enter c: -9
x1: (1.8369701987210297e-16+3j)
x2:	(1.8369701987210297e-16-3j)	
nrg@dmz:~/python$

'''
