height = int(input("Please input your height in cm: "))
weight = int(input("Please input your weight in kg: "))
bmi =  int(weight/(height**2*0.0001))

if bmi<16:
    print("Severely Underweight")
elif bmi<18.5:
    print("Underweight")
elif bmi<25:
    print("Normal")
elif bmi<30:
    print("Overweight")
else:
    print("Obese")
