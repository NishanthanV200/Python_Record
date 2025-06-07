# You are using Python
n1=int(input())
n2=int(input())
power=pow(n1,n2)
print(power)
l=[]
for i in range(1,n2+1):
 l.append(pow(n1,i))
print(l)
print(sum(l))