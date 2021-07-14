def drawIsoscelesTriangle(n): 

    for i in range(n + 1):
        numSpace = n - i
        print (' ' * numSpace + '* ' * i)

drawIsoscelesTriangle(10)