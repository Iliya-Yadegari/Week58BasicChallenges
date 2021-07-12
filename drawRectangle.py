def drawRectangle(w,h):
    widthL = ''
    asterik = '*'
    
    for i in range(w):
        widthL += asterik
    
    for i in range(h):
        print(widthL)

drawRectangle(10,5)