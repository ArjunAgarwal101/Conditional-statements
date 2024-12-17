weight=int(input("Enter your weight in kg's:   "))
height=int(input("Enter your height in cm:     "))
BMI=weight/(height/100)**2
if BMI<=18.4:
       print("you are underweight")
elif BMI>=24.9:
       print("you are normal")
elif BMI>=29.9:
       print("you are overweight")
elif BMI>=34.9:
       print("you are severly overweight")
elif BMI>=39.9:
       print("you are obese")
elif BMI>=40:
       print("you are severly obese")

