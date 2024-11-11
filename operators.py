#OPERATORS IN PYTHON
#Arithmetic operators

x=12
y=3

#addition
print("x+y = ",x+y)

#subtraction
print("x-y = ",x-y)

#multiplication
print("x*y = ",x*y)

#division
print("x/y = ",x/y)

#modulo, reminder
print("x % y = ",x%y)

#exponent
print("x**2 = ",x**2 )

#floor division
print("x//y = ",x//y)

#---------------------------------------------------------------------------
#Assignment operators

# =
a=2
print("a =",a)

# +=
a+=2
print("a+=2 = ",a)

# -=
b=5
b-=2
print("b-=2 = ",b)

# *=
b=3
b*=2
print("b*=2 = ",b)

# /=
b=3
b/=2
print("b/=2 = ",b)

# %=
b=3
b%=2
print("b%=2 = ",b)

# **=
b=3
b**=2
print("b**=2 = ",b)

# //=
b=3
b//=2
print("b//=2 = ",b)

# &=
b=3
b&=2
print("b&=2 = ",b)

# |=
b=3
b|=2
print("b|=2 = ",b)

# ^=
b=3
b^=2
print("b^=2 = ",b)

# >>=
b=3
b>>=2
print("b>>=2 = ",b)

# <<=
b=3
b<<=2
print("b<<=2 = ",b)

# :=
#while (x := input("Enter something: ")) != "stop":
#   print(f"You entered: {x}")
    
#----------------------------------------------------------------------------------------------------
#Comparison operator

#==
x=2
y=2
print("x==y =", x==y)

#!=
print("x!=y =", x!=y)

#>
x=5
y=4
print("x>y =", x>y)

#<
print("x<y =",x<y)

#<=
x=2
y=2
print("x<=y =", x<=y)

#>=
x=2
y=2
print("x>=y =", x>=y)

#-----------------------------------------------------------------------------------------------
# logical operators
#and
x=5
print("(x>0 and x<6) = ",x>0 and x<6)

#or
x=5
print("(x<0 or x==5) = ",x<0 or x==5)

#not
x=5
print("not(x<0 and x==5)",not(x<0 and x==5))

#--------------------------------------------------------------------------------------------------
#Identity operators
# is - to check the same objects
s=["jam","butter"]
t=["jam","butter"]
u=s
print("s is u =",s is u)
print("s is t =",s is t)
print("s == t =",s == t)

#is not
print("s is not t =",s is not t)

#----------------------------------------------------------------------------------------------------
#Membership operators
# in
str1="Made in India"
print("India" in str1)

#not in
print("Made" not in str1)

#------------------------------------------------------------------------------------------------
#Bitwise operators
# &
x=2
y=2
print("x&y =", x&y)

# |
print("x|y =", x|y)

# ^
print("x^y =", x^y)

#~
print("~x =", ~x)

#>>
x=5
x=x>>3
print("x>>3 =",x)

#<<
x=5
x=x<<3
print("x<<3 =",x)