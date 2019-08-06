
# Lets do a simple example for that of elseif

age=input("enter you age: ")
age=int(age)

if 0<age<=3:
    print("ticke price is: Free")
elif 3<age<=10:
    print("Ticket price is : 90")
elif 10<age<=60:
    print("Ticket price is: 200")
else:
    print("ticket price is: 400")