def Calculate_Area(name):
    name = name.lower()
    if name == 'rectangle':
        l = float(input("Length:  "))
        b = float(input("Breadth:  "))
        rect_area = l * b
        print("The area of", name, "is", rect_area)
    elif name == 'square':
        s = float(input('Side:  '))
        sqr_area = s * s
        print('The area of',name, 'is', sqr_area)
    elif name == 'circle':
        pi = 3.14
        r = float(input('Radius:  '))
        cir_area = pi * r**2
        print('The area of', name, 'is', cir_area)
    elif name == 'triangle':
        B = float(input('Base:  '))
        H = float(input('Height:  '))
        tri_area = 0.5 * B * H
        print('The area of', name, 'is', tri_area)
    else:
        print('Invalid shape')
print('Welcome to the area founder.')
print('Calculate the area for : Square, Triangle, Rectangle, Circle')
shape_name = input('Enter the name of the shape:  ')
Calculate_Area(shape_name)

