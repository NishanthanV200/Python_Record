# You are using Python
def is_prime(num):
 if num <=1:
  return False
 for i in range(2,int(num**0.5)+1):
  if (num%i)==0:
   return False
 return True
n=int(input())
p={}
num=2
count=1
while count<=n:
 if is_prime(num):
  p[count]=num
  count+=1
 num+=1
print(p)