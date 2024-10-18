
#Piedra papel tijera, 2 jugadores ,mejor de tres: 
contador1=0
contador2=0

while contador1 < 3 and contador2 < 3:


    J1=int(input("Elije jugador 1: 1-Piedra, 2-Papel, 3-Tijera"))
    J2=int(input("Elije jugador 2: 1-Piedra, 2-Papel, 3-Tijera"))

    if J1 > 3 or J2 > 3:
        print("Número invalido")
    elif J1 <= 0 or J2 <= 0:
        print("Número invalido")
    elif J1 == 1 and J2 == 3:
        contador1 += 1
        print("Gana jugador 1 (Piedra vs Tijera)")
    elif J1 == 2 and J2 == 1:
        contador1 += 1
        print("Gana jugador 1 (Papel vs Piedra)")
    elif J1 == 3 and J2 == 2:
        contador1 += 1
        print("Gana jugador 1 (Tijera vs Papel)")
    elif J2 == 1 and J1 == 3:
        contador2 += 1
        print("Gana jugador 2 (Piedra vs Tijera)")
    elif J2 == 2 and J1 == 1:
        contador2 += 1
        print("Gana jugador 2 (Papel vs Piedra)")
    elif J2 == 3 and J1 == 2:
        contador2 += 1
        print("Gana jugador 2 (Tijera vs Papel)")
    else:
        print("Empate")
if contador1 == 3:
    print("Mejor de 3: jugador 1")
elif contador2 == 3:
    print("Mejor de 3: jugador 2")