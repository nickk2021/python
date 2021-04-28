class coche:
  #atributos o propiedades (variables)
  #caracteristicas del coche
    color = "rojo"
    marca = "ferrari"
    modelo = "aventador"
    velocidad = 300
    caballaje = 500
    plaza = 2
    
    def __init__(self,color,marca,modelo,caballaje,velocidad,plaza):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.caballaje = caballaje
        self.plaza

    # metodos, son acciones que hacen el objeto (coche) (funciones)

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1 
    
    def getVlocidad(self):
        return self.velocidad
