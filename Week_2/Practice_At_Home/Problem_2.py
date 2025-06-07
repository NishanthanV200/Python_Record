# You are using Python
def fact(num):
 f=1
 for i in range(1,num+1):
  f*=i
 return f
n=int(input())
for i in range(1,n+1,2):
 num=fact(i)
 sumofdigit=0
 w=str(num)
 for j in w:
  sumofdigit+=int(j)
 print(f"{i}! = {num}, sum of digits = {sumofdigit}")