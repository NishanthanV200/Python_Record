# You are using Python
n=int(input())
if(n>100 and n<=200):
 print(f"Rs. {(n-100)*5}")
elif(n<=100):
 print(f"Rs. {n*0}")
else:

 print(f"Rs. {(100*5)+((n-200)*10)}")