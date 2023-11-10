operation = int(input("please enter:\n 1: if you want to go from Argentine pesos to dollars\n 2: if you want to go from Colombian pesos to dollars\n 3: if you want to go from Mexican pesos to dollars"))


if operation == 1:
    value = float(input("Enter the value money:"))
    dollars = value / 350
    print ("its value in dollar is:{}". format(dollars) )
elif operation == 2:
    value = float(input("Enter the value money:"))
    dollars = value / 3940
    print ("its value in dollar is:{}". format(dollars) )
elif operation == 3:
    value = float(input("Enter the value money:"))
    dollars = value / 17.13
    print ("its value in dollar is:{}". format(dollars) )
else:
    print("the number entered is not valid")
