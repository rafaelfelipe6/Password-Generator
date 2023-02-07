from caracteres import letters, numbers, symbols, key_logo
import random
print(key_logo)
print("""Bem vindo ao gerador de senhas aleatorias PyPassword!
O script ira gerar uma senha aleatoria para você contendo letras, números e simbolos.
""")
password = ""

# Função para concatenar e randomizar os caracteres da lista de acordo com a entrada no input


def character_random(qty, list):
    global password
    for _ in range(qty):
        password += random.choice(list)


# Sera executado caso o úsuario digite um número inteiro
try:
    # Solicita ao usuario a quantidade de letras na senha
    qt_letters = int(input("Quantos letras você deseja na senha? "))
    character_random(qty=qt_letters, list=letters)

    # Solicita ao usuario a quantidade de números
    qt_numbers = int(input("Quantos números? "))
    character_random(qty=qt_numbers, list=numbers)

    # Solicita ao usuario a quantidade de simbolos
    qt_symbols = int(input("Quantos simbolos? "))
    character_random(qty=qt_symbols, list=symbols)

    # Embaralha a ordem em que os tipos de caracteres são exibidos
    random_password = list(password)
    random.shuffle(random_password)
    random_password = ''.join(random_password)
    print(f'A senha gerada é {random_password}')

# Sera executado caso o úsuario não digite um número inteiro
except ValueError:
    print("por favor, digite um número inteiro")
