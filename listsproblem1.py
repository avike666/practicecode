b = ["banana", "apple", "microsoft"]
print(b)

#lets swap the first item in the list with the last
#item in the list:

temp = b[0]
b[0] = b[2]
#temp = b[2]
b[2] = temp
print(b)
