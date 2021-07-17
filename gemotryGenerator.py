def menu():

    menu_out = int(input(' This program draws the following shapes:\n1) Horizontal Line\n2) Vertical Line\n3) Rectangle\n4) Left slant right angle triangle\n5) Right slant right angle triangle\n6) Isosceles triangle '))

    if menu_out == 1:
        n = int(input('Enter your width: '))

        line = ''
        asterik = '*'

        for i in range(n):
            line += asterik
        print(line)
        
    if menu_out == 2:
        n = int(input('Enter your height: '))
        for i in range(n):
            print('*')
            
    if menu_out == 3:
        widthL = ''
        asterik = '*'

        w = int(input('Enter your width: '))
        h = int(input('Enter your height: '))

        for i in range(w):
            widthL += asterik

        for i in range(h):
            print(widthL)
            
    if menu_out == 4:
        h = int(input('Enter your height: '))
        triangle = ''
        asterik = '*'

        for i in range(h):
            triangle += asterik

            print(triangle)
            
    if menu_out == 5:

        h = int(input('Enter your height: '))

        for i in range(0,h):

            for x in range(0,h - i):
                print(" ",end = "")

            for y in range(0,i + 1):
                print("*",end = "")

        print()

    if menu_out == 6:
        h = int(input('Enter your height: '))
    
        for i in range(h + 1):
            numSpace = h - i
            print (' ' * numSpace + '* ' * i)


menu()