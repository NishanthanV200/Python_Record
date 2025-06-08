k = int(input())
# Dictionary to count appearances
count = {}
for _ in range(k):
 members = list(map(int, input().split()))
 unique_members = []
 for m in members:
  if m not in unique_members:
   unique_members.append(m)
 for m in unique_members:
  if m in count:
   count[m] += 1
  else:
   count[m] = 1
# Members in exactly one club
result = []
for m in count:
 if count[m] == 1:
  result.append(m)
# Output as a set and the sum
print(set(result))
print(sum(result))