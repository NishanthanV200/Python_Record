# You are using Python
n1=int(input())
n2=int(input())
for i in range(n1,n2+1):
 sum=0
 for j in range(1,i):
    if(i%j==0):
        sum+=j
    if(sum==i):
        print(sum)