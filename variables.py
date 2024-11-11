x = str(3)    
y = int(3)    
z = float(3)
_s= "string"

print(x,y,z,_s,sep=" ")

x,y=2,3
print("x:",x,"y:",y)

#global varaiable
x=5
def func():
    x=3
    print("local value:",x)

func()
print("global value:",x)

#global keyword
def para():
    global y
    y=5
    print("inside function y=",y)
    
para()
print("outside function y=",y)

#local varaiable
def localvar():
    p=6
    print("local vraiable", p)
    
localvar()
p=9
print(p)