#===============IMPORT's=========================
import random
#===============FUNCIONES========================
#Función para saludar al jugador 
def saludar_jugador(nombre, vida):
    print(f"{nombre} tiene {vida} puntos de vida")
#Función de estado del jugador
def estado_de_salud(vida):
    if vida <= 0 : 
        print("Estás muerto")
    elif vida > 0 and vida < 10:
        print("CUIDADO! Tienes poca vida")
    else:
        print("Estas en buen estado de salud ")
    return vida > 0
#===============VARIABLES GLOBALES===============
vida_jugador = 20
nombre_jugador = "Héctor"
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
while sala_actual <= 5:
    if sala_actual ==  1: 
            while enemigos[0]['vida'] > 0 and vida_jugador > 0:
                print("En combate")
                enemigos[0]['vida']= enemigos[0]['vida'] - ataque_jugador
                if enemigos[0]['vida'] <=0:
                    print(f"La vida del {enemigos[0]['nombre']} es {enemigos[0]['vida']}")
                    if vida_jugador > 0:
                        print(f"Ganaste la pelea contra el {enemigos[0]['nombre']}")
                    elif vida_jugador <=0:
                        print(f"perdiste la pelea contra el {enemigos[0]['nombre']}")
                        break
                    print("Pasas a la siguiente sala")
                    break
                else:
                    print(f"La vida del {enemigos[0]['nombre']} es {enemigos[0]['vida']}")
                    vida_jugador = vida_jugador - enemigos[0]['ataque']
    elif sala_actual == 2:
        print(f"Sala {sala_actual}: ramdom")
    elif sala_actual == 3:
        while enemigos[1]['vida'] > 0 and vida_jugador > 0:
                        print("En combate")
                        enemigos[1]['vida']= enemigos[1]['vida'] - ataque_jugador
                        if enemigos[1]['vida'] <=0:
                            print(f"La vida del {enemigos[1]['nombre']} es {enemigos[1]['vida']}")
                            if vida_jugador > 0:
                                print(f"Ganaste la pelea contra el {enemigos[1]['nombre']}")
                            elif vida_jugador <=0:
                                print(f"perdiste la pelea contra el {enemigos[1]['nombre']}")
                                break
                            print("Pasas a la siguiente sala")
                            break
                        else:
                            print(f"La vida del {enemigos[1]['nombre']} es {enemigos[1]['vida']}")
                            vida_jugador = vida_jugador - enemigos[1]['ataque']
                            saludar_jugador(nombre_jugador, vida_jugador)
                            estado_de_salud(vida_jugador)
    elif sala_actual == 4:
        print(f"Sala {sala_actual}: ramdom")
    elif sala_actual == 5:
        while enemigos[2]['vida'] > 0 and vida_jugador > 0:
                        print("En combate")
                        enemigos[2]['vida']= enemigos[2]['vida'] - ataque_jugador
                        if enemigos[2]['vida'] <=0:
                            print(f"La vida del {enemigos[2]['nombre']} es {enemigos[2]['vida']}")
                            if vida_jugador > 0:
                                print(f"Ganaste la pelea contra el {enemigos[2]['nombre']}")
                            elif vida_jugador <=0:
                                print(f"perdiste la pelea contra el {enemigos[2]['nombre']}")
                                break
                            print("Pasas a la siguiente sala")  
                            break
                        else:
                            print(f"La vida del {enemigos[2]['nombre']} es {enemigos[2]['vida']} puntos de vida")
                            vida_jugador = vida_jugador - enemigos[2]['ataque']
    sala_actual += 1
sigue_vivo = estado_de_salud(vida_jugador)

if sigue_vivo:
    print("Ganaste el juego")
else: 
    print("perdiste el juego")