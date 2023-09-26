#introductory message
print("This program uses your inputs to calculate the area of a triangle in square meters.")
print("It will notify you if the area equates larger than 40.0 m\u00b2.")
print("Floats are supported and will not be rounded up or down.\n")

# ask user for length
bl = input("insert base length: ")
# typecast to ensure l is a float
bl = float(bl)

# ask user for height
h = input("insert height: ")
# typecast again like above
h = float(h)

#echo the user input
print("you have entered:", bl,"m for base length and", h,"m for height\n")

#calculate the area using bl and h

#declare x as 0.5 to get the 1/2 part of the equation in
x = 0.5
final = x*bl*h
#typecast final as needed
final = float(final)

print("using your values, the area of the triangle is", final,"m\u00b2")

if (final > 40.0):
    print ("the area of these given values is above 40.0 m\u00b2")
    
print("\nprogram by Stephen Colletta for CPE 1000 class")