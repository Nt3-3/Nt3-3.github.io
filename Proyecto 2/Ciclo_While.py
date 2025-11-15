import random
print("Juego de tirar dados")
activado=True
resultado=0
tiradas=int(input("Cuantas veces quieres tirar los dados? (Indicar en caracteres): "))
# Ciclo
while activado==True:
    # Tiradas y Valores
    tiradas=tiradas-1
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    suma=dado1+dado2
    resultado+=suma
    # Resultado
    print(f"El resultado del primer dado es {dado1}")
    print(f"El resultado del segundo dado es {dado2}")
    print(f"\nLa suma de las tiradas es {resultado}")
    resultado=0
    if tiradas==0:
        break
    # Seguir o no
    #if seguir==2:
       # print("El juego terminara ahora, adios")
        #exit()