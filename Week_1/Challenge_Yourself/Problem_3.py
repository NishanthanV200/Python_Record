# You are using Python
f=float(input())
n=int(input())
dis=f-(f*0.10)
bon=dis*0.35
frnd=(dis-bon)/(n-1)
print(f"Cost after a 10% discount: {dis:.2f}\nFriend with a 35% bonus pays:{bon:.2f}\nEach of the other friends pays: {frnd:.2f}")