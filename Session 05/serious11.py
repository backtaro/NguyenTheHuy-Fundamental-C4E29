def is_inside(a,b):
    x1 = a[0] 
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    width = b[2]
    height = b[3]
    x3 = x2 + width
    y3 = y2 + height

    if x2<=x1<=x3:
        if y2<=y1<=y3:
            return True
    else:
        return False

print(is_inside([200, 120], [140, 60, 100, 200]))