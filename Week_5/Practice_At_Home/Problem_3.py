# You are using Python
n=int(input())
e=list(map(int,input().split()))
p=[(e[i],e[i+1])for i in range(n-1)]
p.append((e[-1],None))
print(tuple(p))