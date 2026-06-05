class rectangle:
    
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length*self.width
    
obj1 = rectangle(20,10)
obj2 = rectangle(30,10)
print(obj1.area())
print(obj2.area())

    