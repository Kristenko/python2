class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def getWidth(self):
        return self.width
    
    def setWidth(self, newWidth):
        self.width = newWidth
    
    def getLength(self):
        return self.length

    def setLength(self, newLength):
        self.length = newLength

    def getPerimeter(self):
        return (self.width * 2) + (self.length * 2)

    def getArea(self):
        return self.width * self.length

r = Rectangle(12, 8)
print(r.getPerimeter())
print(r.getArea())
#1