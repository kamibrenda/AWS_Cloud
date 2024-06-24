# concatenate string and vars

firststring = "Reject" 
Secondstring = "The"
Thirdstring = "FinanceBill"  
Fourthstring = firststring + Secondstring + Thirdstring
print(Fourthstring)

# in-built function use - 1 var
name = input("What is your name?")
print(name)

# in-built function use - >1 var
name = input("What is your name?")
color = input("What is your favourite color?")
animal = input("What is your favourte animal?")
print("{}, you like a {} {}!".format(name, color, animal))
