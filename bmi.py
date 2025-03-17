#BMI CALC
Weight=63
height=1.75
bmi=Weight / height**2

if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi > 24.9:
    print("Narmal")
elif bmi >= 25 and bmi < 29.9:
    print("Overweight")
elif bmi >= 30 and bmi < 34.9:
    print("Obese")
elif bmi >= 18.5 and bmi < 25:
    print("Obese")
elif bmi >= 35 and bmi < 39.9:
    print(" Severely Obese")
else:
    print("  morbidly Obese")





