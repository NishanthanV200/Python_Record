# You are using Python
n=int(input())
steps=0
while(n!=1):
 if n%2==0:
  n=n//2
 else:
  n=(n*3)+1
 steps+=1
 if steps >100:
  print("Exceeded 100 steps. Exiting...")
  break
if steps<100:
 print(f"Steps taken to reach 1: {steps}")