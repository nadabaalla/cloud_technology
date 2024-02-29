"""
a) Create an empty list called n.
b) Add 2 and 4 into the list.
c) Print the list.
d) Add 0, 1 and 3 in proper order.
e) Print the list.
f) Add 5 in proper order.
g) Print the list.
h) Remove 0 from the list.
i) Print the list.
j) Remove and print 2 from the list.
k) Print the list.
l) Remove and print 4 from the list.
m) Print the list.
n) Add all the removed numbers and print the sum.
o) Change the first item to 100 and last item to 9.9.
p) Copy the list n to a newNum list.
q) Clear the list n.
r) Print the original list, n and the newNum list.
s) Delete the list n.
"""
#a
n=[]
#b
n.extend([2, 4])
#c
print(n)
#d
n.insert(0,0), n.insert(1,1), n.insert(3,3)
#e
print(n)
#f
n.insert(5,5)
#g
print(n)
#h
n.remove(0)
#i
print(n)
#j&k
rev1=(n.pop(1))
#l&m
rev2=(n.pop(2))
#n
print(rev2)
sum_removed=rev1+rev2
print(sum_removed) #Add all the removed numbers and print the sum.
#o
n.insert(0,100)
n.insert(4,99)
print(n)
#p
newlist=list(n)
print("newlist :", newlist)
n.clear()
print("newlist :", newlist)
#q
print(n)
del n[:]







