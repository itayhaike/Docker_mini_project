class Rectangle:
    count=0

    def __init__(self, side1, side2):
        Rectangle.count+=1
        self.class_side1=side1
        self.class_side2=side2



    def name(self):
        print("the first side is: ",self.class_side1)
        print("the secound side is: ", self.class_side2)


    def __del__(self):
        Rectangle.count-=1

if __name__=="__main__":
    rect1 = Rectangle(5, 6)
    print(f"The mount of rectangle is {Rectangle.count}")
    print(f"rect1 side 1 :{rect1.class_side2} and side 2 : {rect1.class_side2}")
    rect2 = Rectangle(3, 3)
    print(f"The mount of rectangle is {Rectangle.count}")
    print(f"rect1 side 1 :{rect2.class_side2} and side 2 : {rect2.class_side2}")
    rect3 = Rectangle(10, 2)
    print(f"The mount of rectangle is {Rectangle.count}")
    print(f"rect1 side 1 :{rect3.class_side2} and side 2 : {rect3.class_side2}")
    rect1.name()
    rect2.name()
    rect3.name()

    rect1._del_()
    print(f' how meny after delete : {Rectangle.count}')





