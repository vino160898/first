print("Welcome To SBI")
Principal=int(input("Deposite Amount ="))
print("Rate_of_intrest_in_annum 6%")
Time=int(input("Time Duration per Annum ="))
SI=(Principal*6*Time)/100
print("SIMPLE AMOUNT"),print(SI)
print("DEPOSITE AMOUNT"),print(Principal)
print("END OF THE YEAR TOTAL AMOUNT"),print(SI+Principal)
print("COMPOUND INTRESTING")
c=(Principal*(1+6/100)**Time)-1
print("INTREST AMOUNT"),print(round(c-Principal,2))
print("DEPOSITE AMOUNT"),print(Principal)
print("END OF THE YEAR TOTAL AMOUNT"),print(round(c,2))

