# You are using Python
s=input()
l=s.split(' ')
w=input()
wc=0
for word in l:

 if((word==w )or(word[0:3]==w[0:3])):
  wc+=1
print(wc)