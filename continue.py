limit = int(input("enter a value:\n"))
x = 0
total = 0

while (x < limit):
    x += 1
    if (x%2 !=0):
        continue
    total += x

print('total run of double number of range 0 - ',limit,'is',total)
