# You are using Python
n1=int(input())
n2=float(input())
print("Initial salaries:\nAlice's salary = {}\nBob's salary = {}".format(n1,n2))
temp=n1
n1=n2
n2=temp
print("\nNew salaries after swapping:\nAlice's salary = {}\nBob's salary ={}".format(n1,n2))