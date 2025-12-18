class Rectangle:
    def __init__(self,width, height):
        
        if width < 0 or height < 0:
            return ValueError ("The value is negative, only positives ones")
        
        self.width=width
        self.height=height

    def get_area(self):
        return self.width*self.height
    
    def get_perimeter(self):
        return 2*(self.width+self.height)
    def __repr__(self):
        return f"Rectangle (width={self.width}, height={self.height})"
try:
    rect= Rectangle(250,300)
    print(rect)
    print("Area:", rect.get_area())
    print("Perimeter:", rect.get_perimeter())
except ValueError as e:
    print(e)
