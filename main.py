from caracteres import letras, numeros, simbolos
import random

senha = ""


def caracter_random(qty, list):
    global senha
    for i in range(qty):
        senha += random.choice(list)


try:
    qt_letras = int(input("Quantos letras? "))
    caracter_random(qty=qt_letras, list=letras)

    qt_numeros = int(input("Quantos números? "))
    caracter_random(qty=qt_numeros, list=numeros)

    qt_simbolos = int(input("Quantos simbolos? "))
    caracter_random(qty=qt_simbolos, list=simbolos)

    senha_aleatoria = list(senha)
    random.shuffle(senha_aleatoria)
    senha_aleatoria = ''.join(senha_aleatoria)
    print(senha_aleatoria)

except ValueError:
    print("por favor, digite um número inteiro")
