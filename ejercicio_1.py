# Ejercicio 1: Escribir un programa en el que se pregunte al
# usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece
# la letra en la frase. 

def main():
    palabra=input("Escriba una palabra: ")
    letrabuscada=input("Ingrese una letra: ")
    
    acumulador=0
    for letra in palabra:
        if letra == letrabuscada:
            acumulador = acumulador+1
    print("La letra "+ letrabuscada + " aparece "+str(acumulador))
if __name__== '__main__':
    main()