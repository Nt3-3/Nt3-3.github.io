import random
print("Juego de tirar dados")
activado=True
# Ciclo
while activado==True:
    # Valores
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    resultado=dado1+dado2
    # Resultado
    print(f"Los valores de los dados son {dado1} y {dado2}. La suma de estos es {resultado}")
    # Decision
    seguir=int(input("Quiere volver a tirar los dados? Si(1)/No(2): "))
    if seguir==2:
        print("El juego terminara ahora, adios")
        exit()