################
# Facundo Bistevins - @FacuBiste
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def cambiar(texto):
    texto2 = texto.swapcase()
    print(texto2)

texto = input("dame un texto: ")
cambiar(texto)

if __name__ == "__main__":
    cambiar()