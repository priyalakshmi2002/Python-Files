
f=open("myfile.txt","w")
f.write("What a nice time it was")
f.close()

f=open("myfile.txt","r")
print(f.read())
f.close()

f=open("myfile.txt","a")
f.write("Had a great time with everyone")
f.close()

f=open("myfile.txt","r")
print(f.read())
f.close()

