num = int(input())
# You are using Python
def digital_root(num):
 s=str(num)
 l=[]
 for i in s:
  l.append(int(i))
 s2=str(sum(l))
 l2=[]

 for i in s2:
  l2.append(int(i))
 return sum(l2)
print(digital_root(num))