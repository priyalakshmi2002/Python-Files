#while loop
i=0
while i<6:
    print(i)
    i+=1
    
#break statement with while loop
i=0
print("Breaks the iteration when i=3")
while i<6:
    print(i)
    if i==3:
        break
    i+=1
    
#continue statement with while loop
i=0
print("continue statement skips i=3")
while i<6:
    i+=1
    if i==3:
        continue
    print(i, end=" ")
print('\n')    

#else statement in while loop 
i=0
while i<6:
    print(i, end=" ")
    i+=1
else:
    print("i is dead")   
print("\n")  
 
#for loop
#for loop for list
things = ['key','lamp','umbrella']
for x in things:
    print(x)
print("\n")    

#for loop for strings
word="marigold"
for x in word:
    print(x)
print("\n")   
  
#break statement in for loop
for y in things:
    print(y)
    if y=="lamp":
        break
print("\n")  
    
#continue statement in for loop
for y in things:
    if y=="lamp":
        continue
    print(y)
print("\n")  
    
#else in for loop
for x in things:
    print(x)
else:
    print("List is empty now")
print("\n")  
   
#nested loops
color=['blue','pink','green']
matcher= ['sky','rose','leaf']
for x in color:
    for y in matcher:
        print(x,y)
print("\n")  

#pass statement in for loop
for x in [0, 1, 2]:
  pass

    