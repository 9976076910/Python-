# Printing the number of words

#Take input from the user
text = input("Enter the text:")

#convert text to list
list = text.split()

#Lenght of the List
length = len(list)

#print the length
print("Total Count of words:" + str(length))
