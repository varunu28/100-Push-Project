def add(m, n):
    #Function for addition
    return m+n

def sub(m, n):
    #Function for subtraction
    return m-n

def mul(m, n):
    #Function for multiplication
    return m*n

def div(m, n):
    #Function for division
    return float(m)/float(n)

def main():
    while(True):
        print("Choose operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")

        operation=raw_input("1/2/3/4: ")

        if operation == '1':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print(str(num1)+"+"+str(num2)+"="+ str(add(num1,num2)))
            break

        elif operation == '2':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print(str(num1)+"-"+str(num2)+"="+ str(sub(num1,num2)))
            break

        elif operation == '3':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print(str(num1)+"*"+str(num2)+"="+ str(mul(num1,num2)))
            break

        elif operation == '4':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print(str(num1)+"/"+str(num2)+"="+ str(div(num1,num2)))
            break

        else:
            print("Enter a valid operation")

if __name__ == '__main__':
    main()
