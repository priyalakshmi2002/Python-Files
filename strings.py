a="Hello"
print(a[0])
print(a[4])
print(a)

#looping through a string
for x in a:
    print(x)

#length of string
print("length of the string is:",len(a))

#check strings using in
txt="Good"
print("o" in txt)
print("f" in txt)

#check strings using not in 
val="Make it possible through your thoughts"
print("it" in val)
print("yours" not in val)

#slicing of strings
b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[:])
print(b[2:])
print(b[-5:-2])

#modifications of strings
#upper()
print(a.upper())

#lower()
print(a.lower())

#strip() removes white space
name="Users wish"
print(name.strip())

#split(), gives a string using separators
print(name.split())

#replace(), replaces the character or string with the given character or string
print(name.replace("U", "u"))

#concatenation of strings
first="Maintain"
second="silence"
print(first+second)
print(first+" "+second)
print(first,second)

#escape characters
escape="we call him as \"superior\""
print(escape)

#string methods
#capitalize()- to capitalize first letter
word="SLEEP"
print(word.capitalize())

#casefold()- converts to lower case
print(word.casefold())

#center()- centers the string
print(word.center(50))

#count()- counts the number of times the particular string is repeated
letters="she got an apple and gave the apple to her friend"
print(letters.count("apple"))

#find()- searches the string and returns the position
textsen= "Hello, welcome to my home."
x = textsen.find("welcome")
print(x)
#find() and index() are same but find() returns -1 if string not found
print(textsen.find("q"))
#print(textsen.index("q"))

#isalnum()- returns true if all the characters are alphanumeric
txt = "Indus12"
x = txt.isalnum()
print(x)

txt="Indus#$23"
print(txt.isalnum())

#isalpha #isdecimal #isdigit
txt="indus"
print(txt.isalpha())
num="893"
print(num.isdecimal())
print(num.isdigit())

#translate()
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

#swapcase()- upper to lower, lower to upper
txt = "MaIn"
print(txt.swapcase())

#title()- converts every first letter to capital
text="Take a piece of paper"
print(text.title())

#zfill()- fills with zero until it covers the characters mentioned
text="44"
print(text.zfill(8))

text="44.000"
print(text.zfill(8))