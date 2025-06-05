# You are using Python
s1=int(input())
s2=int(input())
s3=int(input())
step1=s1&s2
step2=step1^s3
step3=step2*3%1000
print(step3)