# You are using Python
n1=int(input())
n2=int(input())
a,b=0,1
count=0
for i in range (n1,n2+1):
 a,b=0,1
 found = False
 while a<=i:
    if a==i:
        found=True
        break
    a,b=b,a+b
    if not found :
        count+=1
print(count)