# You are using Python
def count_substrings(text,substring):
 count=0
 s=text.split()
 for i in s:
  if(substring in i):
   count+=1
 return count
text=input()
substring=input()
print(f"The substring '{substring}' appears {count_substrings(text,substring)}times in the text.")