#Task-1 using dictionaries- CONTACT BOOK APPLICATION
contact_book={} #globally declaring a dictionary

#function to add contact
def add_contact():
    name=input("Enter the name:")
    number=input("Enter the contact number:")
    contact_book.update({name:number})

#function to remove contact
def remove_contact():
    val=input("Enter the name of the contact to be deleted:")
    if(val in contact_book):
        del(contact_book[val]) #deletion of contact
        print("Contact deleted successfully")
    else:
        print(f"Contact of {val} does not exist")

#function to lookup a contact
def lookup_contact():
    name1=input("Enter name of the contact:")
    if(name1 in contact_book):
        y=contact_book[name1]
        print(f"{name1}:",y)    
    else:
        print(f"Contact of {name1} does not exist")           

#function to display all the contacts
def display_contacts():
    list1= contact_book.keys()  
    for x in list1:
        print(f"{x}:",contact_book[x])
    else:
        print("Empty record")    
    #print(contact_book.items())
        
#function for the contact book application       
while(True):
    #Prints the list of options
    print("\nOptions for you to choose",
          "\n1 : Add a contact",
          "\n2 : Remove a contact",
          "\n3 : Search for a contact",
          "\n4 : Display all contacts",
          "\n5 : Exit")
    
    #input to select a choice
    num=(input("Enter any one choice (1-5): "))
    
    #condition based operation
    if(num=='1'):
        add_contact()
        print("Contact added successfully")
    elif(num=='2'):
        remove_contact()    
    elif(num=='3'):
        lookup_contact()
    elif(num=='4'):
        display_contacts()
    elif(num=='5'):
        break
    else:
        print("Enter a valid choice")
#prints when function exits        
print("Logged out from Contact book application")