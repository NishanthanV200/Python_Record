# You are using Python
n=int(input())
sumeven=0
sumodd=0
for i in range(0,n+1):
 if(i%2==0):
    sumeven+=i

 else:
    sumodd+=i

print(f"Sum of even numbers from 1 to {n} is {sumeven}")
print(f"Sum of odd numbers from 1 to {n} is {sumodd}")