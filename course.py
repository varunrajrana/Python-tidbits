class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.h=height
        self.r=radius
        
    def volume(self):
        volume=3.14*(self.r**2)*self.h
        print(volume)
    
    def surface_area(self):
        sa=(2*3.14*self.r*self.h)+(2*3.14*self.r**2)
        print(sa)

c = Cylinder(2,3)

c.volume()
