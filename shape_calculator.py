class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        s = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        for i in range(0, self.height):
            for j in range(0, self.width):
                s += "*"
            s += "\n"
        return s

    def get_amount_inside(self, shape):
        return int(self.get_area() / shape.get_area())

    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self):
        return "Square(side={})".format(self.width)
