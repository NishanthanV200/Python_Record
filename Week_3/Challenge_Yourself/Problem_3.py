# You are using Python
l=input()
l1=[]
l2=l.split()
for i in l2:
 l1.append(int(i))
print(f"List1: {l1}")
n=int(input())
if(n in l1):
 l1.remove(n)
 print(f"List after removal: {l1}")
else:
 print("Element not found in the list")
l3=input()
l4=l3.split()
for i in l4:
 l1.append(int(i))
print(f"Final list: {l1}")