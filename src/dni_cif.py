class Dni:
    def __init__(self, cadena=""): # cadena no tiene ningun valor
        self.dni = cadena
        self.numeroSano = None
        self.letraSana = None

    def getDni(self):
        return self.dni
    
    def getNumeroSano(self):
        return self.numeroSano
    
    def getLetraSana(self):
        return self.letraSana