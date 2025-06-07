def analyze_string(input_string):
# You are using Python
 #Type your code here
 u=l=d=s=0
 for let in input_string:
  if let.isupper():
   u+=1
  elif let.islower():
   l+=1
  elif let.isdigit():
   d+=1
  else:
   s+=1
 return u,l,d,s
input_string = input()
uppercase_count, lowercase_count, digit_count, special_count =analyze_string(input_string)
print("Uppercase letters:", uppercase_count)
print("Lowercase letters:", lowercase_count)
print("Digits:", digit_count)
print("Special characters:", special_count)