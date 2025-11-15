print("Juego de aventura")
# Preguntar personaje
personaje=input("Ingrese el personaje seleccionado: ")
# Preguntar numero de vidas
vidas=int(input("Ingrese la cantidad de vidas con las que jugara: "))
# Mostrar mensajes de dificultad
if vidas>=5:
    print(f"Su personaje es {personaje}, con {vidas}. Esta jugando en la dificultad FACIL")
elif vidas==3 or vidas==4:
    print(f"Su personaje es {personaje}, con {vidas}. Esta jugando en la dificultad MEDIA")
elif vidas==1 or vidas==2:
    print(f"Su personaje es {personaje}, con {vidas}. Esta jugando en la dificultad DIFICIL")
else:
    print("Este numero no es valido. Por favor reinicie el juego.")
    exit()