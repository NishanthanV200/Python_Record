# You are using Python
l=eval(input())
lneg=[]
lpos=[]
for i in l:
 if(i<0):
  lneg.append(i)
 elif(i>=0):
  lpos.append(i)
print("List =",lneg+lpos)