num = int(input())
# You are using Python
def sum_digits(n):
 s=str(n)
 l=[]
 for i in s:
  l.append(int(i))
 return sum(l)
sum = sum_digits(num)
print(sum)