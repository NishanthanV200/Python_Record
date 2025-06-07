# You are using Python
s=input()
def compress_string(*args):
 s=args[0]

 compressed=""
 count=1

 for i in range(1,len(s)+1):
  if i<len(s) and s[i]==s[i-1]:
   count+=1
  else:
   compressed+=s[i-1]+(str(count) if count>1 else "")
 count=1
 return compressed
print(compress_string(s))