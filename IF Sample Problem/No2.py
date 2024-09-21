wt_lb = float(input("Weight in Pound: "))
ht_in = float(input("Height in Inches: "))
BMI = round((703 * wt_lb) / (pow(ht_in, 2)), 1)

if BMI < 18.5 :
    print("Underweight")
elif BMI >= 18.5 and BMI < 25 :
    print("Normal")
elif BMI >= 25 and BMI < 30 :
    print("Overweight")
else:
    print("Obese")