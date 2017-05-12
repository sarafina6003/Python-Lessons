salary = input("Enter your salary :")

if salary<=11180:
    tax=0.1 *salary
    netpay = salary -tax
elif salary>=11181 and salary>=21714:
    tax = 0.15 * salary
    netpay = salary - tax
elif salary>=21715 and salary>=32248:
    tax = 0.2 * salary
    netpay = salary - tax
elif salary>=32249 and salary>=42782:
    tax = 0.25 * salary
    netpay = salary - tax
elif salary >42782:
    tax = 0.3 * salary
    netpay = salary - tax
print "Your tax is "+str(tax)
print  "Your netpay is " +str(netpay)



