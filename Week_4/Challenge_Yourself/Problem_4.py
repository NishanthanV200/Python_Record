# You are using Python
n=int(input())
s=input()
s1=s.split()
l=[]
for i in s1:
 l.append(int(i))

check=lambda a,b:a%b
evencount=oddcount=0
len(l)
for i in l:
 if(check(i,2)==0):
  evencount+=1
 else:
  oddcount+=1
print(evencount)
print(oddcount)