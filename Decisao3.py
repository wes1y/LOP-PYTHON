# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

import os
os.system('cls')

letra1 = input(
    'Digite seu sexo com as letras "F" para Feminino ou "M" para Masculino')

if letra1 == 'M' or 'm':
    print('Sexo Masculino')
elif letra1 == 'F' or 'f':
    print('Sexo Feminino')
else:
    print('Sexo Invalido')
