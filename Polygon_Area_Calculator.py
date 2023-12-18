class Rectangle:

  def __init__(self, width=0, height=0):
    self.width = width
    self.height = height

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2 * self.width) + (2 * self.height)

  def get_diagonal(self):
    return (self.width**2 + self.height**2)**0.5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      string = (("*" * int(self.width)) + "\n") * int(self.height)
      return string

  def get_amount_inside(self, shape):
    return int((self.get_area()) / (shape*shape))


class Square(Rectangle):

  def __init__(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    return f'Square(side={self.width})'

  def set_side(self, side):
    self.width = side
    self.height = side

def validate_input_num(input_description=": "): 
    while True:
        try:
            variable=float(input(input_description))
        except:
            print('===Invalid Input===')
            continue
        if type(variable)==float:
            break
    return variable


print("===This program is my version of the freeCodeCamp Polygon area calculator project=== ")

rectagle=Rectangle()
rectagle.set_width(validate_input_num("Enter the widht: "))
rectagle.set_height(validate_input_num("Enter the height: "))
print(f'The area of the rectangle is {rectagle.get_area()}')
print(f'The perimeter of the rectangle is {rectagle.get_perimeter()}')
print(f'The diagonal of the rectangle is {rectagle.get_diagonal()}')
print("How many squares can you fit in the rectangle?")
side=validate_input_num("Enter the side of the square: ")
print(f'You could fit {rectagle.get_amount_inside(side)} squares in the rectangle')
print("")
print(rectagle.__str__())
print(rectagle.get_picture())
square=Square(side)
print(f'The area of the square is {square.get_area()}')
print(f'The perimeter of the square is {square.get_perimeter()}')
print(f'The diagonal of the square is {square.get_diagonal()}')
print("")
print(square.__str__())
print(square.get_picture())
