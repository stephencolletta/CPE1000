#more demonstration

x = 22.1

if ((x > 50.0) or (x < 30.0)):
    print("above 50.0")
    print("enjoy statements")

print("this statement will always appear")

# the other way to do these ifs/ors ie. else if (elif)
if (x > 30.0):
    print("Cranberries")
# elif is ONLY checked when the if above is not true
elif (x > 20):
    print("You are above 20....not 30")
    
# equivalent code to above
if (x > 30):
    print("Cranberries")

if ((x > 20) and (x <= 30)):
    print("You are above 20....not 30")
    
# addition of else - else only happpens if above statements false
if (x > 100):
    print("x above 100..")
elif (x > 80):
    print("x above 80..")
else:
    print("test")
