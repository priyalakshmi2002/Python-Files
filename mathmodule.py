import math
print("Square root:",math.sqrt(64))
print("Factorial:",math.factorial(5))
print("pi:",format(math.pi,".2f"))
print("Radians to degrees:",format(math.degrees(2),".2f")) #degree of 2 
print("Degrees to radians:",format(math.radians(30),".2f")) #radians of 30
print("Sine of 2:",math.sin(2))#sine of radians
print("Cosine of 1:",math.cos(1))#cosine of radians
print("Tangent of 0.23:",math.tan(0.23))#tangent oof radians
print(dir(math))

import random
print(random.randint(0,5))

#print ranndom floating point number between 0 and 1
print(random.random())

list2=['tsrijjj',9,3,'kdjk']
print(random.choice(list2))

from datetime import date
import time
# Returns the number of seconds since the
print(time.time())  

# Converts a number of seconds to a date object
print(date.fromtimestamp(994554889))
print(date.today())
today = date.today()
print(today.year)
print(today.day)
print(today.month)

from datetime import time
#hours minutes and seconds 
Time = time(11, 34, 56)
 
print("hour =", Time.hour)
print("minute =", Time.minute)
print("second =", Time.second)
print("microsecond =", Time.microsecond)

# Creating Time object
Time = time(12,24,36,1212)
 
# Converting Time object to string
Str = Time.isoformat()
print("String Representation:", Str)
print(type(Str))

from datetime import datetime 
# Calling now() function
today = datetime.now()
 
print("Current date and time is", today)