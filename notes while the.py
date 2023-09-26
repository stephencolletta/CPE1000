#loop example - while loop
#while loops execute until the bordering statement becomes false

#single equals to assign a value. double equals to compare a value.
x = 1

while (x==1):
    print(" Spam")
    #this x = 2 doesn't matter. while is only checked at the start of a new loop ie. new iteration
    x = 2
    x = input("save me and input a new value for x:")
    x = int(x)
    
#lets countdown after asking the user for an input
#beginning from a number
y = input("input a number to count from:")
y = int(y)

while (y >= 0):
    print(y)
    y = y - 1