import random
# Definicion
def dado():
    # Tiradas y Valores
    tiradas=int(input("Cuantas veces quieres tirar los dados? (Indicar en caracteres): "))
    resultado=0
    for i in range(tiradas):
        dado=random.randint(1,6)
        resultado+=dado
    # Regresar
    return resultado