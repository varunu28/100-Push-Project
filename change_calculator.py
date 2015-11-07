''' 1 dollar=100cents
    1 quarter =25 cents
    1 penny=1 cent
    1 dime =10cents
'''

def change_left(cost,amt):
    return amt-cost

def specification(change):
    a=[]
    
    if change>=100:
        n=change/100
        change=change%100
        a.append(n)
    else:
        a.append(0)

    if change >=25:
        n=change/25
        change=change%25
        a.append(n)
    else:
        a.append(0)

    if change>=10:
        n=change/10
        change=change%10
        a.append(n)
    else:
        a.append(0)

    a.append(change)

    return a

while True:
    print "Enter the cost in cents:"
    cost = input()
    print "Enter the amt in cents:"
    amt=input()
    
    if type(cost)==int and type(amt)==int:
        if amt>cost:
            change = change_left(cost,amt)
            change_dist = specification(change)
            print "You have "+str(change_dist[0])+ " dollars, " +str(change_dist[1])+" quarter, "+str(change_dist[2])+" dimes and "+str(change_dist[3])+ " cents "+" left with you."
            break
        elif amt<cost:
            print "You have to pay more"
            break
        else:
            print "You have no change left."
            break
        

    
        
        
