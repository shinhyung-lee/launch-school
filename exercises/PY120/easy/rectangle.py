class Rectangle:
    def __init__(self, width, height):
        self.width = width 
        self.height = height 
    
    @property 
    def width(self):
        return self._width 
        
    @width.setter 
    def width(self, width):
        self._width = width 
        
    @property 
    def height(self):
        return self._height 
    
    @height.setter 
    def height(self, height):
        self._height = height 
        
    @property 
    def area(self):
        return self.width * self.height 
    
    @area.setter 
    def area(self, area):
        self._area = area 

rect = Rectangle(4, 5)

print(rect.width == 4)        # True
print(rect.height == 5)       # True
print(rect.area == 20)        # True