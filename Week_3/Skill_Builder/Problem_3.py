# You are using Python
n=int(input())
l=[]
for i in range(0,n):
 num=int(input())
 l.append(num)
print("List after appending elements:",l)
i=int(input())
p=l[i]
del l[i]
print("List after popping last element:",l)
print("Popped element:",p)