# You are using Python
nums=list(map(int,input().split()))
ch=int(input())
s=sorted(set(nums),reverse=True)
print("{"+",".join(map(str,s))+"}")
if ch==1:
 print(max(nums))
elif ch==2:
 print(min(nums))
elif ch==3:
 n1=int(input())
 if n1 in nums:
  nums.remove(n1)
 u=sorted(set(nums),reverse=True)
 print("{"+",".join(map(str,u))+"}")
else:
 print("Invalid choice")