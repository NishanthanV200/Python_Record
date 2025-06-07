# You are using Python
n1=int(input())
s=input()
s1=s.split()
l=[]
for i in s1:
 l.append(int(i))
divi=lambda i,n:i%n
count3=0
l3=[]
for i in range(len(l)):
 if(not divi(l[i],3)):
  count3+=1
 l3.append(l[i])
print(count3)
count5=0
l5=[]
for i in range(len(l)):
 if(not divi(l[i],5)):
  count5+=1
 l5.append(l[i])
print(count5)
print(sum(l3))
print(sum(l5))