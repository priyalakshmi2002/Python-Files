num1= 40
num2= 30

#if condition for greater than(>)
if (num1>num2):
    print(f"{num1} is greater than {num2}")
    
#if condition for greater than or equal(>=)
num1=40
num2=40
if (num1>=num2):
    print(f"{num1} is greater than or equal {num2}")
    
#equal to (==)
if(num1==num2):
    print("yes its equal")
    
#lesser than (<)
num1= 40
num2= 30
if(num2<num1):
    print(f"{num2} is lesser than {num1}")

#less than or equal (<=)
if(num2<=num1):
    print(f"{num2} is lesser than or equal {num1}")

#not equal to(!=)    
if(num1!=num2):
    print("true")
    
#if else statement
if(num1<num2):
    print("true part")
else:
    print("false part")
    
#elif statement
if(num1<num2):
    print(f"{num1} is less than {num2}")
elif(num1==40):
    print(f"num1 is {num1}")
else:
    print("error")
    
#one line if else statement, ternary operator
print(f"{num1} is greater") if num1>num2 else print(f"{num2} is greater")

#and keyword in condition
if(num1>num2 and num1!=num2):
    print("True")
    
#or keyword in condition
if(num1>num2 or num1==num2):
    print("True")
    
#NOT keyword in condition
if( not num1<num2):
    print("True")
    
#Nested if
age=18
if age>=18:
    print("adult")
    if age<18:
        print("child")
    else:
        print("oldage")

#pass statement
if(num1<num2):
    pass
print("Successful!")

#Match case, replacement of switch case in python
# This code runs only in python 3.10 or above versions
def number_to_string(argument):
    match argument:
        case 0:
            return "zero"
        case 1:
            return "one"
        case 2:
            return "two"
        case default:
            return "something"
 
head = number_to_string(2)
print(head)
