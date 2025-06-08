# You are using Python
def count(l,n):
 count=0
 for i in l:
  if i==n:
   count+=1
 return count
n=int(input())
l=[]
for i in range(n):
 l.append(int(input()))
l2=[]
d={}
for j in range(len(l)):
 if(l[j] not in l2):
  l2.append(l[j])
  d[l[j]]=count(l,l[j])
print(d)
values=d.values()
print("Total Unique IDs: ",len(values))
avg=sum(values)/len(values)
print(f"Average Frequency: {avg:.2f}")