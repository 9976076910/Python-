## Printing pyramid of numbers

# getting user input
rows = int (input(" No of rows:"))

for i in range (1,rows +1):
    for j in range (1,i+1):
        print(j,end="")
    print("\n")
