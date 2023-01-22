# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

import os
os.system('cls')

numeromaioquezero = int(input('Digite um número: '))

if numeromaioquezero > 0:
    print('Esse número é positivo.')
else:
    print('Esse número é negativo.')
