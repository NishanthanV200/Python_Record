# You are using Python
n=int(input())
l=[]
for i in range(0,n):
 l.append(int(input()))
l.sort()
l2=[]
for j in range(0,len(l)):
 if(j%2==0):
  l2.append(l[j]**3)
 else:
  l2.append(l[j]**2)
l2[0]=0
print(f"Original List: {l}\nReplaced List: {l2}")