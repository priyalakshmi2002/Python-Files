class student:
    name="ram"
    def __init__(self,dob,reg):
        self.dob=dob
        self.reg=reg
    
    def details(self):
        print("The name of the student is:",self.name)
        print("The dob:",self.dob)
        print("The reg no.:",self.reg)
        
    def __del__(self):
        print("thankyou")
        
n=student("15-9-2002","1234")
n.details()