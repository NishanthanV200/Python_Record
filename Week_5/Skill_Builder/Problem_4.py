# You are using Python
n=int(input())
l=[]
for i in range(2):
 l1=input()
 l.append(l1)
s1=l[0].split(',')
s2=l[1].split(',')
s=[]
for i in range(len(s1)):
 s.append(int(s1[i])+int(s2[i]))
t=tuple(s)
print(t)