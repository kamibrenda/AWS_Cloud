#function definition 
def monday_greetings(name):
    return f"Hello Good Morning {name}, REJECT FINANCE BILL "
names = ["William", "Joy", "Christine", "Michelle"]
for name in names:
    print(monday_greetings(name))


    

#ver_2
def monday_greetings(name):
    return "Hello Good Morning {} , REJECT FINANCE BILL".format(name)
names = ["William", "Joy", "Christine", "Michelle"]
for name in names:
    print(monday_greetings(name))