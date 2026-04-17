def grossSalary():
    bs = float(input("Enter Basic Salary: "))
    da = (bs * 70) / 100
    ta = (bs * 30) / 100
    hra = (bs * 10) / 100
    grossSal = bs + da + ta + hra
    print("Gross Salary:", grossSal)

grossSalary()
