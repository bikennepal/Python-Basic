# replace() method
#find() method

string="She is beautiful and she is a good dancer"

# print(string.replace("is","was"))

# If you have more than one word in a string than follow the below statemnts
# print(string.find("is"))

is_pos1=string.find("is") #for finding the string position.
is_pos2=string.find("is",is_pos1 + 1)
print(is_pos2)


