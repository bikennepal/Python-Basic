# practice for loop
# ask number from user like 1234
# calculate the number

 
n=input("enter a number: ")
total=0

for i in range(0,len(n)):
    total+= int(n[i])

print(total)