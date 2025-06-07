# You are using Python
n1=int(input())
n2=int(input())
sum1=0
for i in range(n1,n2+1):
 w=str(i)
 if w!=w[::-1]:
    for j in str(i):
        sum1+=int(j)

print(sum1)