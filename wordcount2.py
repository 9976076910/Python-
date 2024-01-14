string = input("Enter the string:")
total = 1
for i in range(len(string)):
    if(string[i] == '' or string == '\n' or string == '\t'):
        total = total + 1
print("Total number of words =",total)
