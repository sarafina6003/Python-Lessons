weight = input("Enter your weight :")
#print (type(weight))
height = input("Enter your height :")
#print (type(height))
if weight<200 and height<=3 and weight>0 and height>0:
    bmi = weight/height**2
    if bmi< 15:
     print("Very severely underweight")

    elif bmi>=15 and bmi<16:
     print("Severely underweight")

    elif bmi >= 16 and bmi < 18.5:
     print("Underweight")

    elif bmi>=18.5 and bmi<25:
     print("Normal(healthy weight)")

    elif bmi >= 25 and bmi < 30:
     print("Overweight")

    elif bmi >= 30 and bmi < 35:
     print("Obese Class I (Moderately obese)")

    elif bmi >= 35 and bmi < 40:
     print("Obese Class II (Severely obese)")

    elif bmi >40:
     print("Obese Class III (Very Severely obese)")

else:
    print ("Enter a reasonable value!")


