import Funciones_Modulo
print("Juego de dados de 2 jugadores")
activado=True
while activado==True:
    # Definicion, primer turno, y retorno
    print("\nTurno del jugador 1")
    resultado=Funciones_Modulo.dado()
    print(f"El resultado de la tirada es {resultado}")
    # Seguir o no
    seguir=input("Quiere seguir jugando? (Y/N)").upper()
    if seguir=="N":
        activado=False
        break
    # Segunda vez
    print("\nTurno del jugador 2")
    resultado=Funciones_Modulo.dado()
    print(f"El resultado de la tirada es {resultado}")
    seguir=input("\nQuiere seguir jugando? (Y/N)").upper()
    if seguir=="N":
        activado=False
print("Adios!")