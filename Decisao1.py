import os
os.system('cls')

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um número: '))

if numero1 > numero2:
    print(f'{numero1} é o maior número digitado.')
else:
    print(f'{numero2} é o maior digitado.')
