# You are using Python
def sc(w,d):
 if d=="Domestic":
  return w*5
 elif d=="International":
  return w*10
 else:
  return w*15
 return None
weight=float(input())
destination=input()
d=["Domestic","International","Remote"]
shipping_cost=None
if weight<0:
 print("Invalid weight. Weight must be greater than 0.")


elif (destination in d):
 shipping_cost=sc(weight,destination)
else:
 print("Invalid destination.")


if shipping_cost is not None:
 print(f"Shipping cost to {destination} for a {weight} kg package:${shipping_cost:.2f}")