class Rectangle:
    #Constructor.
    def __init__(self, height, width):
        self.height = height
        self.width = width
    #Calculate the area.
    def area(self):
        return self.height * self.width
    #Calculate the perimeter
    def perimeter(self):
        return (2 * self.height) + (2 * self.width)
#Create instance
r1 = Rectangle(10, 35)
#r1.height = 20

#Another instance
r2 = Rectangle(2, 5)



print(f"Area of r1 = {r1.height} x {r1.width} = {r1.area()}")  
print("The area of the other rectangle is", r2.area())
print("The perimeter of rectangle 1 is", r1.perimeter())     