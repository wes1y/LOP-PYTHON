import os
os.system('cls')

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A última letra do seu nome é: {nome[-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não tem espaços')

else:
    print('Desculpe, você deixou campos vazios.')

# commit_teste1
# commit_teste2
# commit_teste3
# commit_teste4
# commit_teste5
