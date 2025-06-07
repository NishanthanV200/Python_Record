# You are using Python
s=input()
n=s.split()
s=0
for i in n:
 for j in i:
  if(j.isdigit()):
   s+=int(j)
if(s>9):
 s1=str(s)
 if(s1[::-1]==s1):
  print(f"{s} Palindrome")
 else:
  print(f"{s} Not palindrome")
else:
 print(s)