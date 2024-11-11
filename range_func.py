#sequence of number with range
for i in range(5):
    print(i, end=" ")
print('\n')

x=range(6)
for i in x:
    print(i, end=" ")
print('\n')

#range function with start and end value where end value is not inclusive
for i in range(1,5):
    print(i,end=" ")
print('\n')

#range function with skip value
for i in range(1,10,2):
    print(i, end=" ")
print('\n')

#range function with steps as negative numbers
for i in range(20,2,-2):
    print(i, end=" ")
print('\n')

#range with the list
fruits = ["apple", "banana", "cherry", "date"]
for i in range(len(fruits)):
    print(fruits[i])

#range with index value
ele = range(10)[0]
print("First element:", ele)

ele = range(10)[-1]
print("\nLast element:", ele)

ele = range(10)[4]
print("\nFifth element:", ele)
