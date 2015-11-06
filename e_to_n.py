from math import e

def e_to_n(n):  #Function to return the value of e limited to n decimal places
    return '%.*f' % (n, e)

while True:
    print "Enter a precision factor between 1 and 50"  # A limit between 1 and 50 for input
    n = input()
    if n>=1 and n<=50:
        print e_to_n(n)
        break


