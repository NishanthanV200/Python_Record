# You are using Python
y1=int(input())
y2=int(input())
for i in range(y1,y2+1):
 if((i%4==0 and i%100!=0) or i%400==0 ):
  print(i)