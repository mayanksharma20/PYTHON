

def da(basic_slary):
    if (basic_salary < 5000):
        da=((basic_salary)*(30/100))        # level 1
    elif(basic_salary>=5000 and basic_salary<10000):
        da=((basic_salary)*(35/100))        # level 2
    else:
        da=((basic_salary)*(40/100))        # level 3

    return da

def hra(basic_salary):
    if (basic_salary < 5000):
        hra=((basic_salary)*(14/100))        # level 1
    elif(basic_salary>=5000 and basic_salary<10000):
        hra=((basic_salary)*(18/100))        # level 2
    else:
        hra=((basic_salary)*(22/100))        # level 3
    return hra

def allowance(da,hra):
    allowance=da+hra
    return allowance

basic_salary=int(input("Enter basic salary: "))
da=da(basic_salary)
hra=hra(basic_salary)
allowance=0
print(allowance)