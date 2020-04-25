coordinate1 = (3,2)
coordinate2 = (8,10)

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2
    
    def distance(self):
        dx=abs(self.coor2[0]-self.coor1[0])
        print(dx)
        dy=abs(self.coor2[1]-self.coor1[1])
        print(dy)
        distance=(dx**2 +dy**2)**0.5
        print(distance)

    def slope(self):
        dx=abs(self.coor2[0]-self.coor1[0])
        print(dx)
        dy=abs(self.coor2[1]-self.coor1[1])
        print(dy)
        slope=dy/dx
        print(slope)
        pass
    
li = Line(coordinate1,coordinate2)

li.slope()
