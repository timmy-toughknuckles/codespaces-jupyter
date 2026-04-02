a = input('Enter the shape you want to calculate (circle, rectangle, triangle, square, parallelogram, trapezoid): ')
if a.lower() == 'circle':
    radius = float(input('Enter the radius of the circle: '))
    area = 3.14159 * radius ** 2
    print('The area of the circle is: ' + str(area))
elif a.lower() == 'rectangle':
    length = float(input('Enter the length of the rectangle: '))
    width = float(input('Enter the width of the rectangle: '))
    area = length * width
    print('The area of the rectangle is: ' + str(area))
elif a.lower() == 'triangle':
    base = float(input('Enter the base of the triangle: '))
    height = float(input('Enter the height of the triangle: '))
    area = 0.5 * base * height
    print('The area of the triangle is: ' + str(area))
elif a.lower() == 'square':
    side = float(input('Enter the side length of the square: '))
    area = side ** 2
    print('The area of the square is: ' + str(area))
elif a.lower() == 'parallelogram':
    base = float(input('Enter the base of the parallelogram: '))
    height = float(input('Enter the height of the parallelogram: '))
    area = base * height
    print('The area of the parallelogram is: ' + str(area))
elif a.lower() == 'trapezoid':
    base1 = float(input('Enter the length of the first base of the trapezoid: '))
    base2 = float(input('Enter the length of the second base of the trapezoid: '))
    height = float(input('Enter the height of the trapezoid: '))
    area = 0.5 * (base1 + base2) * height
    print('The area of the trapezoid is: ' + str(area))
else:
    print('Invalid shape entered. Please enter one of the following: circle, rectangle, triangle, square, parallelogram, trapezoid.')