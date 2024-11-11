#print statement
print("hello")

#input function
name= input("Enter your name: ")
print(name)

#input as string
num=input("enter a number: ")
print(num)
print(type(num))

#input as num
num= int(input("enter a number: "))
print(num)
print(type(num))

#print statement with multiple output
name = "Alice"
age = 30
print("Name:", name, "Age:", age)
print(type(age))

# end Parameter with '@'
print("Python", end='@')
print("GeeksforGeeks")

# Seprating with Comma
print('G', 'F', 'G', sep=' ')

# for formatting a date
print('09', '12', '2016', sep='-')

# another example
print('pratik', 'geeksforgeeks', sep='@')

#print using % operator
print("The age is %d" %age)

#multiple inputs
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)