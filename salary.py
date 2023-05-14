basic_salary=int(input("Enter basic salary: "))

if (basic_salary < 5000):
    da=basic_salary*0.3
    hra=basic_salary*.14
    gross_salary=basic_salary+da+hra
    deduction=(gross_salary*0.03)+(gross_salary*0.04)
    final_salary=gross_salary-deduction
    print("Final salary at level 1 is: ",final_salary)

elif(basic_salary>=5000 and basic_salary<10000):
    da=basic_salary*0.35
    hra=basic_salary*.18
    gross_salary=basic_salary+da+hra
    deduction=(gross_salary*0.05)+(gross_salary*0.06)
    final_salary=gross_salary-deduction
    print("Final salary at level 2 is: ",final_salary)

else:
    da=basic_salary*0.4
    hra=basic_salary*.22
    gross_salary=basic_salary+da+hra
    deduction=(gross_salary*0.07)+(gross_salary*0.08)
    final_salary=gross_salary-deduction
    print("Final salary at level 3 is: ",final_salary)

