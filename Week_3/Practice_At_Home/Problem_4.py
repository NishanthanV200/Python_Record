# You are using Python
n=input()
uc=lc=dc=sc=0
for l in n:
 if(l.isupper()):
  uc+=1
 if(l.islower()):
  lc+=1
 if(l.isdigit()):
  dc+=1
 if((not l.isalpha())and(not l.isdigit())):
  sc+=1

 print(f"Uppercase letters: {uc}\nLowercase letters: {lc}\nDigits: {dc}\nSpecialcharacters: {sc}")