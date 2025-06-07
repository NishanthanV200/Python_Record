weight = float(input())
height = float(input())
# You are using Python
def calculate_bmi(w,h):
 bmi=w/(h**2)
 print(f"Your BMI is: {bmi:.2f}")
calculate_bmi(weight, height)