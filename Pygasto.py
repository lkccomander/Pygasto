class Pygasto:
    """description of class"""

 


    """Constructor"""
    """description of class"""

    def __init__(self, p_gastodesc, p_gastocomercio, p_gastodate, p_gastomonto,p_gastomisc,p_gastomisc2):
        
        
        self.gastodesc = p_gastodesc
        self.gastocomercio = p_gastocomercio
        self.gastodate = p_gastodate
        self.gastomonto =  p_gastomonto
        self.gastomisc = p_gastomisc
        self.gastomisc2 = p_gastomisc2


    



    """Destroyer"""
    def __del__ (self):
        pass


    """Methods"""

    def writegasto(self):
        pass
    def delgasto(self):
        pass
    def updategasto(self):
        pass
    def traergastos(self):
        pass

    def DisplayData(self):
        print("\nGasto Id: ", self.gastodesc)
        print("Descripcion de Gasto: ",self.gastodesc)
        print("Comercio: ",self.gastocomercio)
        print("Fecha del Gasto: ",self.gastodate)
        print("Monto del Gasto:", self.gastomonto)
        print("Misc 1:",self.gastomisc)
        print("Misc 2:",self.gastomisc2)









