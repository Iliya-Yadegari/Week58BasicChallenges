def menu():

    menu_out = int(input(' This program draws the following shapes:\n1) Horizontal Line\n2) Vertical Line\n3) Rectangle\n4) Left slant right angle triangle\n5) Right slant right angle triangle\n6) Isosceles triangle '))

    if menu_out == 1:
        menu_1()

    elif menu_out == 2:
        menu_2()

    elif menu_out == 3:
        menu_3()

    elif menu_out == 4:
        menu_4()

    elif menu_out == 5:
        menu_5()

    elif menu_out == 6:
        menu_6()

def menu_1():
        n = int(input('Enter your width: '))

        line = ''
        asterik = '*'

        for i in range(n):
            line += asterik
        print(line)

def menu_2():
    n = int(input('Enter your height: '))
    for i in range(n):
        print('*')

def menu_3():
        widthL = ''
        asterik = '*'

        w = int(input('Enter your width: '))
        h = int(input('Enter your height: '))

        for i in range(w):
            widthL += asterik

        for i in range(h):
            print(widthL)

def menu_4():
        h = int(input('Enter your height: '))
        
        triangle = ''
        asterik = '*'

        for i in range(h):
            
            triangle += asterik

            print(triangle)    

def menu_5():

    h = int(input('Enter the height: '))
    
    for i in range(0,h):
        
        for x in range(0,h-i):
            print(" ",end = "")
        
        for y in range(0,i+1):
            print("*",end = "")
        
        print()

def menu_6():
        
    h = int(input('Enter your height: '))

    for i in range(h + 1):
            numSpace = h - i
            print (' ' * numSpace + '* ' * i)    

menu()