# You are using Python
d={}
n=int(input())
for i in range(n):
 l=[]
 n1=input()
 n2=n1.split()
 for j in n2:
  l.append(int(j))
  k=l[0]
  l2=[]
 for a in range(1,len(l)):
  l2.append(l[a])
  l3=[sum(l2),max(l2)]
  d[k]=l3
print(d)