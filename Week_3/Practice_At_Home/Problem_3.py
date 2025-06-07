# You are using Python
n=int(input())
l=[]
n2=input()
n2=n2.split(' ')
for i in n2:
 if(int(i)>=0):
  if not i in l:
   l.append(int(i))
l.sort()
i=1
while True:
 if i not in l:
  print(i)
  break
 i+=1