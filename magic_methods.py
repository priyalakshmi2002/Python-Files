#magic methods inherited by int class
 
#__repr__ in python defines how the object is presented as string
class String:    
    # magic method to initiate object
    def __init__(self, string,start,stop):
        self.string = string
        self.start = start
        self.stop = stop
           
    #returns string object
    def __repr__(self):
        return 'Object: {}'.format(self.string)
    
    def __add__(self, other):
        print(type(other))
        return f"{self.string}john" + other 
    
    def __call__(self):
        print("Instance is called via special method")
        
    def __eq__(self,val):
        return self.string == val.string
    
    def __iter__(self):
        for num in range(self.start,self.stop+1):
            yield(num)

if __name__ =='__main__':
    string1 = String('Hello',8,9)
    print(string1)
    print(string1 +"kailash")
    string1()
    string2 = String('Vishnu',5,6)
    string3 = String('Vishnu',5,6)
    print(string2==string3)
    string4 = iter(String("hello",4,7))  
    print(next(string4))
    print(next(string4))
    print(next(string4))  
    print(next(string4)) 

