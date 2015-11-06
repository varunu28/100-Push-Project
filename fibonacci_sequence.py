'''What is Fibanacci Sequence??
Sequence: 0,1,1,2,3,5,8,13...
As you can see that in the sequence we get the next term by adding previous two terms
Read more at : https://en.wikipedia.org/wiki/Fibonacci_number
'''

def fibonacci_sequence(n):  # Function to generate the sequence and store it in a list
    seq_list=[]                           # The list which contains the sequence
    a=0
    b=1
    c=0
    seq_list.append((a))
    seq_list.append((b))
    i=1
    while i<n-1:                         # Logic to generate the sequence
        c = a + b
        seq_list.append((c))
        a = b
        b = c
        i+=1
    return seq_list

while True:                              # To check that input is an integer greater than 0
    print "Enter a positive integer: "
    n = input()
    if type(n) == int and n > 0:
        print fibonacci_sequence(n)       # Printing the sequence
        break
    
    
    
