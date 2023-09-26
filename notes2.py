print("test")

#both are identical inferred vs explicit, int or float etc
n = 5
n = int(5)

print("math math n equals", n)
print ("now we post the class which is", type(n))
#a demonstration of object oriented programming, in which object n is of class int

x = float(5.6)
print("recall that x is", x, "and it's class is", type(x))

Information = 7.19500433
print("now recall that Information is", Information, "with a class", type(Information))

#introducing a new variable and new class type "str" string
message = "This is not a message..."
print(message, "this is pure lies")
print(type(message))

#let's get decisive with if statements
#if checks if the following statement is true, and follows indents if so.
#if only impacts what's indented below it
if (n > 4):
    print("value of n is above 4")
    if (x > 2):
        print("printception")
        
#free from impact of "If"
print("also here's some words")
