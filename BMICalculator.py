height = float(input("Enter your height in m: "))
weight = int(input("enter your weight in kg: "))

result = round(weight / height ** 2)

if result <18.5:
    print(f"Your bmi is {result}, you are underweight")
elif result <=25:
    print(f"Your bmi is {result}, you have a normal weight")
elif result <= 30:
    print(f"Your bmi is {result}, you are overweight")
elif result <= 35:
    print(f"Your bmi is {result}, you are obese")
else:
    print(f"Your bmi is {result}, you are clinically obese")

