"""
ejercicio 5 :
crear una lista conel contenido de esta tabla:
ACCION      AVENTURA        DEPORTE
GTA         CRASH           FIFA21
GOD         ASSINS          PRO21
PUGS       PRINCE OF        moto gp 21


Mostrar esta informacion ordenada
"""

tabla =[
    {
        "categoria": "ACCION",
        "juego": ["GTA", "Call of duty", "pug"]
    },
    {
        "categoria": "AVENTURA",
        "juego": ["crash", "assins", "prince of percia"]
    },
    {
        "categoria": "DEPORTE",
        "juego": ["fifa 21", "pro 21", "moto gp 21"]
    }

]

for categoria in tabla: 
    print(f"--------{categoria ['categoria']}---------")
    for juego in categoria['juego']:
        print(juego)