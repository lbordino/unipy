from math import sqrt as sq
def areaeper(a,b):
    perim = (a+b)*2
    area = a*b
    diagonale = sq(a**2 + b**2)
    return perim, area, diagonale
print(areaeper(2,3))

