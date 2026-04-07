a = 0
b = 0
x = 0
y = 0
z = 0


a = input("Which shape would you like to calculate? Square, circle, triangle, rectangle, parallelogram, trapazoid: ")

if "square" == a.lower():
    x = int(input("What is the length of one side? "))
    print("The perimeter of the square is " + str(x*4))
elif "circle" == a.lower():
    x = int(input("What is the radius of the circle? "))
    print("The perimeter of the circle is " + str(2*3.14*x))
elif "triangle" == a.lower():
    x = int(input("What is the length of the first side? "))
    y = int(input("What is the length of the second side? "))
    z = int(input("What is the length of the third side? "))
    print("The perimeter of the triangle is " + str(x+y+z))
elif "rectangle" == a.lower():
    x = int(input("What is the length of the rectangle? "))
    y = int(input("What is the width of the rectangle? "))
    print("The perimeter of the rectangle is " + str(2*x+2*y))
elif "parallelogram" == a.lower():
    x = int(input("What is the length of the parallelogram? "))
    y = int(input("What is the width of the parallelogram? "))
    print("The perimeter of the parallelogram is " + str(2*x+2*y))
elif "trapazoid" == a.lower():
    x = int(input("What is the length of the first side? "))
    y = int(input("What is the length of the second side? "))
    z = int(input("What is the length of the third side? "))
    b = int(input("What is the length of the fourth side? "))
    print("The perimeter of the trapazoid is " + str(x+y+z+a))
else:    print("That is not a valid shape.")