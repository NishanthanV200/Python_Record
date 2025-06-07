s=input()
v=['a','e','i','o','u']
for i in s:
 if((i.lower() in v) or not i.isalpha() ):
    continue
else:
    print(i,end=" ")