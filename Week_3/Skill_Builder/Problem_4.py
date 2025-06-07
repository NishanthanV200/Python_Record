# You are using Python
s=str(input())
n1=int(input())
n2=int(input())
ans=s[n1:n2+1]
if((not n2<n1)and ( not (n1)>len(s))):
 print(ans)
else:
 print("Invalid start and end positions")