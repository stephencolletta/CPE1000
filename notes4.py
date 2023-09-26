# using/programming python functions
# functions are essentially combining steps into one entity

# many functions are built in already, like print
# print = function, "quoted stuff" is the argument
print("Goodbye, world!")

# some built in functions might need a library/"module" to be imported

import math

# this function gets 9, gets the sqrt of it, and puts it in x
# 9 is the argument, and sqrt belongs to math module
x = math.sqrt(9)
print(x)

# it is possible to write your own functions
# "def" is used for this purpose
# mind the indent. functions always have () after their name
# this takes no args and prints
def greet():
    print("Pixies...")
    
# to actually use this function it must be called like so
greet()
greet()
greet()

# this function adds numbers
# place arguments in the parenthesis to tell the function what to add
# it does not matter what you name the arguments
# result, num1, num2 ONLY exist within adding function
# they are DELETED upon function conclusion

# the first option around this is to place print in the function
# the other option is demonstrated below, using return
def adding(num1, num2):
    result = num1 + num2
    return result

# to run this, call it like before
value1 = adding(3, 8)
print(value1)
value2 = adding(3.5, 1.9)
print(value2)

# you can also print it directly without variables
print(adding(3.3, 5.5))

# recall y = int(3) object y of class int
# another example of function is the member function of a class ie "methods"
# creating info, an object of class list
info = list([33.3, 6.6, 99.9])
#alternatively
info = [33.3, 6.6, 99.9]

print(info)
print(type(info))

# classes hold data, but also have methods/member functions
# these are things they can do
# one example is class list's ability to sort itself
info.sort()
print(info)
# another example is append
info.append(600.51)
print(info)

#demonstrating pop which removes the value at the selected position
#pop counts from zero not one, same for all others that specify pos
info.pop(2)
print(info)

#insert places that value at the specified position, again counting from zero
info.insert(2, 5.11)
print(info)
info.sort()
print(info)
