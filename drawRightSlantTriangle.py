def drawRightSlantTriangle(h):

    for i in range(0,h):
    
        for x in range(0,h - i):
            print(" ",end = "")
    
        for y in range(0,i + 1):
            print("*",end = "")
        
        print()

drawRightSlantTriangle(10)