class Rectangle:
    def __init__(self,height,width):
        self._width=width
        self._height=height

    def length(self):
        return f"{self._height*self._width:.1f} cm"

    @property
    def width(self):
        return f"{self._width:.1f} cm"

    @property
    def height(self):
            return f"{self._height:.1f} cm"

    @height.setter
    def height(self,new_height):
        if new_height<0:
            print("height should be more than 0")
        else:
             self._height=new_height
             print("height updated sucesfully!")

    @width.setter
    def width(self,new_width):
        if new_width<0:
            print("width should be more than 0")
        else:
                self._width=new_width
                print("width updated sucesfully!")

    @width.deleter
    def width(Self):
         del Self._width
         print("width deleted succesfully")

obj=Rectangle(4,6)
obj.height=3
obj.width=4
print(obj.height)
print(obj.width)
print(obj.length())


del obj.width
