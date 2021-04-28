

class coche:

    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventor"
    velocidad = 300
    caballaje = 500
    plaza = 2 


    def setcolor(self, color):
        self.color = color
    
    def getcolor(self):
        return self.color
    
    def setmodelo(self,modelo):
        self.modelo = modelo

    def getmodelo(self):
        return self.modelo 

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getvelocidad(self):
        return self.velocidad


coche = coche()
coche.setcolor("amarillo")
coche.setmodelo("murcielago")

print(coche.marca, coche.getmodelo(), coche.getcolor())
print("velocidad actual: ", coche.velocidad)


coche2 = coche ()
print(coche2.getcolor())
