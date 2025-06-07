x=input()
x1=x.split()
l=[]
peak=[]
for i in x1:
 l.append(int(i))
for i in range(len(l)):
 if i==0 and l[i]> l[i+1]:
  peak.append(l[i])
 elif i==len(l)-1 and l[i]> l[i-1]:
  peak.append(l[i])
 elif 0<i<len(l)-1 and l[i]>l[i-1] and l[i]>l[i+1]:
  peak.append(l[i])
print("Peaks: ",peak)