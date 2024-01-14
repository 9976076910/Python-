## Program for removing vowel from the string

#getting user input 
word = input("Enter the string:")

#converting to lower case
string = word.lower()

#declaring vowel
vowel = "aeiou"

print("Input String:",string)

for char in string:
    if char in vowel:
        string = string.replace(char,"")
print(" New Output String: ",string)
