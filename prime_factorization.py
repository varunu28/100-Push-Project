def prime_gen(n):
	a=[]
	i=2
	while i <= n:
		if n%i == 0:
			a.append(i)
		i+=1
	return a

def print_gen(a):
	i=0
	ans = ""
	while i < len(a):
		ans=ans+str(a[i])+" "
		i+=1
	return ans

while True:
	print "Enter a number greater than 0: "
	n = input()

	if type(n)==int:
		if n>0:
			a=prime_gen(n)
			ans=print_gen(a)
			if len(ans)>0:
				print ans
			else:
				print "No prime factors for this"
			break
                          
                
                
                
		

