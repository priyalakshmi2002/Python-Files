#iterator
tuple1=("akash","ram","karthik")
tuple_iter=iter(tuple1)
print(next(tuple_iter))
print(next(tuple_iter))
print(next(tuple_iter))

#iterating with strings
string1="variations"
trial=iter(string1)
print(next(trial))
print(next(trial))
print(next(trial))
print(next(trial))
print(next(trial))
print(next(trial))
print(next(trial))
print(next(trial))
print(next(trial))
print(next(trial))

#iterator using loop
mytuple = ("apple", "banana", "cherry")
#x is an iterator object
for x in mytuple:
  print(x)
  
#class as an iterator
class MyNumbers:
      def __iter__(self):
        self.a = 1
        return self

      def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#stopiteration
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
  print(x)