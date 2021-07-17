def drawIsoscelesTriangle(h): 

    for i in range(h + 1):
        numSpace = h - i
        print (' ' * numSpace + '* ' * i)

drawIsoscelesTriangle(10)