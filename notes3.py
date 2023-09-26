# input a variable
y = input("put something in: ")
# without changing anything, y will always be a string
# typecast it to make it an integer - inputting non-numbers breaks the code
y = int(y)

#echoing the input
print("you just entered:", y)
print("the class of what you entered is:", type(y))

#use double equals to determine if two numbers are equal
#a single equals will declare the variable instead
#demonstration of an if/or statement using |
if ((y == 5) | (y == 6)):
    print("print due to 5/6")
    
#replicate the above statement using ands
if (y > 4) & (y < 7):
    print ("you have used and instead of an or")
    
#alternative method
    if (y >= 5) & (y <= 6):
        print ("you've used ands instead of or again")
    
#demonstration of and using & to get a "range"
if (y > 2) & (y < 5):
    print("y is above 2 and below 5")
