def bin_to_dec(bin_inp):
    ans_dec=0
    bin_inp=bin_inp[::-1]
    n=len(bin_inp)
    i=0
    while i<n:
        ans_dec+=int(bin_inp[i])*pow(2,i)
        i+=1
    return ans_dec

def dec_to_bin(dec_inp):
    ans_bin=''
    while dec_inp>0:
        ans_bin=ans_bin+str(dec_inp%2)
        dec_inp=dec_inp/2
    return ans_bin[::-1]
    

while True:
    print "Enter a binary number: "
    bin_inp = input()
    print "Enter a decimal number: "
    dec_inp=input()
    if type(bin_inp)==int and type(dec_inp)==int:
        print "The value of "+ str(bin_inp) + " in decimal is: "+ str(bin_to_dec(str(bin_inp)))
        print "The value of "+ str(dec_inp) + " in binary is: "+ str(dec_to_bin(dec_inp))
        break
