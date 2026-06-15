import math

class MyPoint:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
    
    def setX(self, x):
        self.__x = x
    
    def getX(self):
        return self.__x
    
    def setY(self, y):
        self.__y = y
    
    def getY(self):
        return self.__y
    
    def setXY(self, x, y):
        self.__x = x
        self.__y = y
    
    def getXY(self):
        return [self.__x, self.__y]
    
    def toString(self):
        return f"({self.__x}, {self.__y})"
    
    def distance(self, x, y):
        return math.sqrt((self.__x - x)**2 + (self.__y - y)**2)
    
    def distancePoint(self, another):
        return math.sqrt((self.__x - another.getX())**2 + (self.__y - another.getY())**2)
