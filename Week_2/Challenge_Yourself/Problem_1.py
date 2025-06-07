# You are using Python
def isPrime(num):
 if num<2:
  return False
 for i in range(2,int(num**0.5)+1):
  if num%i==0:
   return False
 return True

def fb(num):
 a,b=0,1
 count=0
 r=[]
 while True:
  fb=a+b
  a,b=b,fb
  if isPrime(fb):
   r.append(fb)
   count+=1
  if count==n:
    break
 print(" ".join(map(str,r)))

n=int(input())
fb(n)