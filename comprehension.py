#list comprehension
list1=[20,25,24,30,35,40,44]  
list2=[i for i in list1 if i%3==0]  
print("The elements obtained are: " ,list2)  

#To find the square of each element
list3=[i**2 for i in list1]
print("The square of each element is: ",list3)

#dictionary comprehension
num=['1','2','3','4','5','6','7']  
days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']  
result_dict = {key:value for (key,value) in zip(num,days)}  
print("The dictionary using comprehension would be: ",result_dict) 
list2=[i for i in days if i!="Thursday"] 
print(list2)

#set comprehension
list1=[20,25,24,30,35,40,44]  
set1={i for i in list1 if i%3==0}
print("The elements obtained in set are:" ,set1)  

#generator comprehension
list1=[12,16,17,20,21,24,28,30,31]  
result_gen=(i for i in list1 if i%2==0)  
for i in result_gen:  
    print("The element which is even in list1 is: ",i)  
    
a = [1,2,3,4,5]
b,c,d,*e=a
print(b)
print(c)
print(d)
print(e)
