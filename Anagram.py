#Program to find anagaram

#Take the input from the user
string1 =input("Enter the first string:")

#Convert it to lower case
str1 = string1.lower()
string2 = input("Enter the Second String:")

str2 = string2.lower()

#Sorting the string
sortedstr1 = sorted(str1)
sortedstr2 = sorted(str2)

if len(str1) == len(str2):
   if sortedstr1 ==sortedstr2:
     print("True")
   else:
     print("False")
else:
    print("False")

