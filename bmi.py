weight = input("Enter your weight :")
#print (type(weight))
height = input("Enter your height :")
#print (type(height))
if weight<200:
    bmi = weight/height**2
    print("Your bmi is "+ str(bmi))
else:
    print ("Enter a reasonable value!")