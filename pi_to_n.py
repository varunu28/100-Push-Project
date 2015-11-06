def pi_to_n(n):
    ans = "3."
    quot = 22/7
    rem = 22%7 
    i=0
    while i<n:
        rem*=10
        ans  = ans + str(rem/7)
        rem = rem%7
        i+=1
    return ans

print "Enter a value of n:"
n = input()
print "The value of pi upto " + str(n) + " decimal places is: " + str(pi_to_n(n))

