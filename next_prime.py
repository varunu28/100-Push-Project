#The Brute force approach
def is_prime(a):
    i=2
    c=1
    while i<=a/2:
        if a%i==0:
            c=0
            break
        i+=1
    return c

def next_prime(n):
    new_n=n+1
    ans=0
    while True:
        if is_prime(new_n)==1:
            ans = new_n
            break
        else:
            new_n+=1
    return ans

while True:
    print "Enter a number greater than 1 or enter 0 if you want to stop: "
    n = input()
    if  type(n)==int and n>1 and n!=0:
            print next_prime(n)
    elif n==0:
        break
    






    
        
        
        
