class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def set_width(self,width):
        self.width = width

    def set_height(self,height):
        self.height = height

    def get_area(self):
        return (self.width*self.height)

    def get_perimeter(self):
        return (2*self.width+2*self.height)

    def get_diagonal(self):
        return((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        output=""
        if max(self.width,self.height)>50:
            return "Too big for picture."
        for x in range(self.height):
            output+=("*"*self.width)+'\n'
        #output+="*"*self.width
        return output

    def __str__(self):
        return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"

    def get_amount_inside(self,shape):
        s = 0
        h = self.height
        w = self.width
        s1=0
        s2=0
        s1 = (h//shape.height*w//shape.width)
        s2 = (h//shape.width*w//shape.height)
        return max(s1,s2)


class Square(Rectangle):
    def __init__(self,Length):
        self.width = Length
        self.height = Length

    def __str__(self):
        return "Square(side="+str(self.width)+")"

    def set_side(self,Length):
        self.width = Length
        self.height = Length
