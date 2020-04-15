class WashingMachine:
    """description of class"""

 


    """Constructor"""
    """description of class"""

    def __init__(self, brandname, modelname, serialname, capacity):
        self.brandname = brandname
        self.modelname = modelname
        self.serialname = serialname
        self.capacity = capacity




    """Destroyer"""
    def __del__ (self):
        pass


    """Methods"""

    def acceptClothes(self):
        pass
    def acceptDetergent(self):
        pass
    def turnOn(self):
        pass
    def turnOff(self):
        pass

    def DisplayData(self):
        print("\nBrandName: ",self.brandname)
        print("Model Name: ",self.modelname)
        print("Serial Number: ",self.serialname)
        print("Capacity: ",self.capacity)







