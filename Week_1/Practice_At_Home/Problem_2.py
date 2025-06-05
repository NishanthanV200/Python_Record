# You are using Python
mb=int(input())
mbps=int(input())
totalsec=(mb*8)//mbps
hr=(totalsec//3600)
minu=(totalsec%3600)//60
sec=totalsec%60
print(f"Download Time: {hr} hours, {minu} minutes, and {sec} seconds")