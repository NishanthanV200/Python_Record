# You are using Python
n=int(input())
ids=[int(input())for _ in range(n)]
ids.sort()
result=[]
group=[ids[0]]
for i in range(1,n):
 if ids[i]==ids[i-1]+1:
  group.append(ids[i])
 else:
  result.append(tuple(group))
 group=[ids[i]]
result.append(tuple(group))
for grp in result:
 if len(grp)==1:
  print(f"({grp[0]})")
else:
 print(tuple(grp))