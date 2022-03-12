#read file
file = open("C:/projects/python/testing/files/m.txt")
print(file.read())
file.close()

#read part of file
file = open("C:/projects/python/testing/files/m.txt")
print(file.read(3))
file.close()

#read parts of file
file = open("C:/projects/python/testing/files/m.txt")
print(file.read(2))
print(file.read())
file.close()

#seek to beginning of file
file = open("C:/projects/python/testing/files/m.txt")
print(file.read(2))
file.seek(6)
print(file.read())
file.close()

#buffer read file
file = open("C:/projects/python/testing/files/m.txt")
file.seek(0,2)
length_of_file = file.tell()
print("length_of_file: ",length_of_file)
file.seek(0)
for i in range(0, length_of_file, 3):
      print(file.read(3))
file.close()

#read line
file = open("C:/projects/python/testing/files/m.txt")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

#read lines
file = open("C:/projects/python/testing/files/m.txt")
lines = file.read().splitlines()
file.close()
print(lines)

##################

file = open("C:/projects/python/testing/files/w.txt","w")
file.close()

file = open("C:/projects/python/testing/files/w.txt","w")
file.write('test write to file1\n')
file.close()
 
file = open("C:/projects/python/testing/files/w.txt","w") 
file.write("test write to file\n")
file.write("more writing to file\n")
file.write("more!!!!\n")
file.close() 

f = open("C:/projects/python/testing/files/w2.txt", "w")
print("test print to file", file=f)
print("no new line problem!", file=f)
f.close()

file = open("C:/projects/python/testing/files/w2.txt", "a")
print("test append print to file", file=file)
file.close()

#####################

file = open("C:/projects/python/testing/files/w2.txt", "r+")
file.truncate(6)
print(file.read())
file.close()

####################

with open("C:/projects/python/testing/files/w3.txt","a") as f:
    print("test append print to file", file=f)

with open("C:/projects/python/testing/files/w3.txt", "r") as f:
      fileStr = f.read()
      print(fileStr)