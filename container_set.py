#set
#no duplicates
#unordered
#unindexed
#unmutable itemns

#create
newSet = {1,2,3,4}
secSet = {1,2,3,4,5,6,7,8,9,8,7,6,5,4}

print(newSet)
print(secSet)

#create from list
setFromList = set([1,2,3,4,3])

print(type(newSet))

#empty set
emptySet = set()
print(type(emptySet))

#ltreating through a set
for i in secSet:
    print (i)

#membership test
print(2 in secSet)
print(32 in secSet)

#addItem
newSet.add(3)
newSet.add(3)
newSet.add(5)
print(newSet)

#add items from lists, sets...
newSet.update([1,2,3,3,2],{5,6,99},(2,567,32))
print(newSet)

#remove item no error
newSet.discard(1)
newSet.discard(4)
newSet.discard(344)
print(newSet)

#remove item with error
#newSet.remove(9)
#print(newSet)

#pop
x = newSet.pop()
print(x)
print(newSet.pop())
print(newSet.pop())
print(newSet)

#clear
newSet.clear()
print(newSet)

#python set operators
set_a = {5,6,7,8,9,10}
set_b = {7,8,9,10,3,45}
print(set_a)
print(set_b)

#Union
print(set_a | set_b)

#intersection
print(set_a & set_b)

#difference
print(set_a - set_b)
print(set_b - set_a)

#symetric difference
print(set_a ^ set_b)

#differnce update
set_a.difference_update(set_b)
print(set_a)
print(set_b)

#disjoin()
set_a = {1,2.3}
set_b = {4,5,6}

print(set_a.isdisjoint(set_b))
set_a.add(6)
print(set_a.isdisjoint(set_b))

#is subset/superset
set_a = {1,2,3}
set_b = {1,2,3,4,5,6}

print(set_a.issubset(set_b))
set_a.add(7)
print(set_a.issubset(set_b))
set_a.discard(7)
print(set_b.issuperset(set_a))


#length
print(len(set_a))
print(len(set_b))


#min/max
print(min(set_b))
print(max(set_b))


#new sorted list
set_b.add(-1)
set_b.add(-5)
set_b.add(67)
print(set_b)
sortedListFromSet = sorted(set_b)
print(sortedListFromSet)
print(type(sortedListFromSet))


#sum
print(sum(set_b))