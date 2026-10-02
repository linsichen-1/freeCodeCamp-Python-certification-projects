class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = self.width * 2 + self.height * 2
        return perimeter
    
    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal

    def get_picture(self):
        if self.width < 50 and self.height < 50:
            picture = f'{"*"*self.width}\n'*self.height
            return picture
        else:
            return 'Too big for picture.'
    
    def get_amount_inside(self, polygon):
        h_number = self.height // polygon.height
        w_number = self.width // polygon.width
        repetition = h_number * w_number
        return repetition

class Square(Rectangle):
    def __init__ (self, side):
        self.width = side
        self.height = side
    
    def __str__(self):
        return f'Square(side={self.width})'
    
    def set_width(self, side):
        self.width = side
        self.height = side
    
    def set_height(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side