N = int(input())
items = []
for _ in range(N):
 item = eval(input())
 items.append(item)
threshold = int(input())
result = []
for _, quantities in items:
 fltered = list(filter(lambda x: x > threshold, quantities))
 result.extend(fltered)
print(*result)