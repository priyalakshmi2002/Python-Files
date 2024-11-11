#example for polymorphism
#one class as India
class India:
    def capital(self):
        print("New Delhi")
 
    def language(self):
        print("variety of languages")
 
    def type(self):
        print("developing country.")

#other class as USA 
class USA:
    def capital(self):
        print("Washington, D.C.")
 
    def language(self):
        print("English")
 
    def type(self):
        print("developed country")

def func(obj):
    obj.capital()
    obj.language()
    obj.type()

#instance for the classes 
obj_ind = India()
obj_usa = USA()
#function call using objects 
func(obj_ind)
func(obj_usa)
