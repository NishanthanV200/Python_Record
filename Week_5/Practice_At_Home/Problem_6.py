# You are using Python
nums=list(map(int,input().split()))
unique_nums=[]
seen=set()
for num in nums:
 if num not in seen:
  unique_nums.append(num)
  seen.add(num)
result=''.join(str(num) for num in unique_nums)
print(result)