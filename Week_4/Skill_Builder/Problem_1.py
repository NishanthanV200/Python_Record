# You are using Python
def is_armstrong_number(number):
 sum=0
 s=str(number)
 length=len(s)
 for i in s:
  sum+=int(i)**length
 if(sum==number):
  return True
 else:
  return False
n=int(input())
if(is_armstrong_number(n)):
 print(f"{n} is an Armstrong number.")
else:
 print(f"{n} is not an Armstrong number.")