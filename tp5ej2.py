################
# Facundo Bistevins - @FacuBiste
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def fibonacci(limite):
        a, b = 0,1
        while a < limite:
            print(a, end='; ')
            a, b = b, a + b

numero = int(input("hasta que numero?: "))
fibonacci(numero)


if __name__ == "__main__":
    fibonacci()
