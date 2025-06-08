# Read frst dictionary
n1 = int(input())
dict1 = {}
order1 = []
for _ in range(n1):
 key = int(input())
 value = int(input())
 dict1[key] = value
 order1.append(key)
# Read second dictionary
n2 = int(input())
dict2 = {}
order2 = []
for _ in range(n2):
 key = int(input())
 value = int(input())
 dict2[key] = value
 order2.append(key)
# Create result dictionary in correct order
result = {}
# First, process keys from dict1 in their input order
for key in order1:
 if key in dict2:
  result[key] = abs(dict1[key] - dict2[key])
 else:
  result[key] = dict1[key]
# Then, add keys unique to dict2 in their input order
for key in order2:
 if key not in dict1:
  result[key] = dict2[key]
# Output result
print(result)