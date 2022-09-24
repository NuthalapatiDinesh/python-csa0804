grade=input("enter the grade(A/C) :")
salary= int(input("enter the salary :"))
if (grade == 'A') and (salary>10000):
    bonus= salary*(5/100)
    print(" total salary is:", bonus+salary)
elif (grade == 'C') and (salary>10000):
    bonus= salary*(10/100)
    print("total salary is:",bonus+salary)
elif (grade == 'A') and (salary<=10000):
    bonus= salary*(7/100)
    print(" total salary is:",bonus+salary)
elif (grade == 'C') and (salary<=10000):
    bonus=salary*(12/100)
    print("total salary is:",bonus+salary)
else:
    print("wrong input")
print("bonus:", bonus)
