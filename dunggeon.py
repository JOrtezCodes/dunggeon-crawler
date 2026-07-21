#===============FUNCIONES========================

#Función para saludar al jugador 
def saludar_jugador(nombre, vida):
    print(f"{nombre} tiene {vida} puntos de vida")

def estado_de_salud(vida):
    if vida <= 0 : 
        print("Estás muerto")
    elif vida > 0 and vida < 10:
        print("CUIDADO! Tienes poca vida")
    else:
        print("Estas en buen estado de salud ")
#===============VARIABLES GLOBALES===============

vida_jugador = 20
nombre_jugador = "Joel"
ataque_jugador = 5
enemigos = [
    {"nombre": "Goblin", "vida": 10, "ataque": 3},
    {"nombre": "Esqueleto", "vida": 8, "ataque": 5},
    {"nombre": "Orco", "vida": 15, "ataque": 10},
]
sala_actual= 1

#===============FLUJO PRINCIPAL==================

#Saludo inicial 
saludar_jugador(nombre_jugador, vida_jugador)

#Bucle de estado de las salas 
while sala_actual <= 5:
    print(f"Estas en la sala {sala_actual}")
    sala_actual += 1

print("llegaste al final de la dunggeon")

for i in range(len(enemigos)):
    print(f"Te estás enfrentando a un {enemigos[i]['nombre']}")
    while enemigos[i]['vida'] > 0 and vida_jugador > 0:
        enemigos[i]['vida']= enemigos[i]['vida'] - ataque_jugador
        print(f"La vida del {enemigos[i]['nombre']} es {enemigos[i]['vida']}")
        vida_jugador = vida_jugador - enemigos[i]['ataque']
        saludar_jugador(nombre_jugador, vida_jugador)
        estado_de_salud(vida_jugador)
    if vida_jugador > 0:
        print(f"Ganaste la pelea contra el {enemigos[i]['nombre']}")
    elif vida_jugador <=0:
        print(f"perdiste la pelea contra el {enemigos[i]['nombre']}")
        break
if vida_jugador <= 0:
    print("perdiste el juego")
else: 
    print("Ganaste el juego")




#===============Test Zone========================



# for enemigo in enemigos:
#     print(f"{enemigo['nombre']} tiene {enemigo['vida']} pupntos de vida y ataca con{enemigo['ataque']} puntos de ataque")