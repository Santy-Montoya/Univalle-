cedula = input("please enter your cedula")
sal_bas = int(input("plase enter your basic wage"))
linkage = int(input("please enter your link year"))

if sal_bas >= 1200000 and linkage >= 1995:
    sal_net = (sal_bas * 6 / 100) - (sal_bas * 4 /100)
elif sal_bas <= 550000 or sal_bas == 1995:
    sal_net = sal_bas * 3 / 100 - (sal_bas * 4 /100)
else:
    sal_net = sal_bas * 4 /100 - (sal_bas * 4 /100)

print(cedula, "your net salary is: {}". format(sal_net))
