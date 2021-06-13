################
# Facundo Bistevins - @FacuBiste
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# formula numero perfecto
# 2^n-1 (2^n - 1)


def perfecto(numero):
    suma = 0

    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    
    if suma == numero:
        print("es perfecto")
    else:
        print("no es perfecto")
    
    

numero = int(input("dame numero: "))
perfecto(numero)

if __name__ == "__main__":
    perfecto()