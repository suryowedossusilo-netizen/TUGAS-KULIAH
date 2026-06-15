import math

class MyPoint:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
    
    def setX(self, x): self.__x = x
    def getX(self): return self.__x
    def setY(self, y): self.__y = y
    def getY(self): return self.__y
    def setXY(self, x, y): self.__x = x; self.__y = y
    def getXY(self): return [self.__x, self.__y]
    def toString(self): return f"({self.__x}, {self.__y})"
    def distance(self, x, y): return math.sqrt((self.__x - x)**2 + (self.__y - y)**2)
    def distancePoint(self, another): return math.sqrt((self.__x - another.getX())**2 + (self.__y - another.getY())**2)


class MyLine:
    def __init__(self, begin, end):
        self.__begin = begin
        self.__end = end
    
    def getBegin(self): return self.__begin
    def setBegin(self, begin): self.__begin = begin
    def getEnd(self): return self.__end
    def setEnd(self, end): self.__end = end
    
    def getBeginX(self): return self.__begin.getX()
    def setBeginX(self, x): self.__begin.setX(x)
    def getBeginY(self): return self.__begin.getY()
    def setBeginY(self, y): self.__begin.setY(y)
    
    def getEndX(self): return self.__end.getX()
    def setEndX(self, x): self.__end.setX(x)
    def getEndY(self): return self.__end.getY()
    def setEndY(self, y): self.__end.setY(y)
    
    def getBeginXY(self): return self.__begin.getXY()
    def setBeginXY(self, x, y): self.__begin.setXY(x, y)
    def getEndXY(self): return self.__end.getXY()
    def setEndXY(self, x, y): self.__end.setXY(x, y)
    
    def getLength(self):
        return self.__begin.distancePoint(self.__end)
    
    def getGradient(self):
        dx = self.__end.getX() - self.__begin.getX()
        dy = self.__end.getY() - self.__begin.getY()
        if dx == 0:
            return float('inf')  # garis vertikal
        return dy / dx
    
    def toString(self):
        return f"MyLine[{self.__begin.toString()}, {self.__end.toString()}]"
