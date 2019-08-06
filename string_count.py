# ask a user name from user
# example : biken Nepal


name=input('enter the user name')
#biken nepal
temp_var=""
i=0
while i < len(name):
    if name[i] not in temp_var:
        temp_var+=name[i]
print(f"{name[i]}:{name.count(name[i])}")
i=i + 1