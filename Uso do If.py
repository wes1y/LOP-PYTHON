import os
os.system('cls')

primeiroValor = input('Digite um valor: ')
segundoValor = input('Digite um valor: ')

if primeiroValor >= segundoValor:
    print(f'{primeiroValor} é maior que o {segundoValor}')
else:
    print(f'{segundoValor} é maior que o {primeiroValor}')
