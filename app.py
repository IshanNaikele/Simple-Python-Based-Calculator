def addition(a,b):
    print(f"The Addition of the numbers {a} and {b} is :{a+b}")

def substraction(a,b):
    print(f"The Subtraction of the numbers {a} and {b} is :{a-b}")

def multiplication(a,b):
     print(f"The Multiplication of the numbers {a} and {b} :{a*b}")
     
def divison(a,b):
    if(b==0):
        print("Division by Zero is not Allowed ")
    else :
        print(f"The Division of the numbers {a} and {b} :{a/b}")
        
     

print("********************************************")
print("Welcome To Python Based Calculator ")
print("********************************************")
 

exit=True

while(exit ):
    try :
       a=int(input("Enter a Number :"))
       b=int(input("Enter a Number :"))
    except :
        print("Enter Valid Value .Only Numeric Value is allowed")
        continue

    print("Which Operation You want to perform ?" )
    print("1.Enter '+' for Addition")
    print("2.Enter '-' for Substraction")
    print("3.Enter '*' forMultiplication")
    print("4.Enter '/' for Divison")
    print("5.Press any other key to Exit ")
    print("\n")
    operation=input("Your Chosen Operation :")
    print("\n")
    
    if operation=="+":
        addition(a,b)
    elif operation=="-":
        substraction(a,b)
    elif operation=="*":
        multiplication(a,b)
    elif operation=='/':
        divison(a,b)
    else :
        print("Exiting Calculator .Thank You!!!")
        exit=False
    print("\n\n")
        
     
        
        
        
        
    
    
 