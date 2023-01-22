# Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar
# ######
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

import os
os.system('cls')

nota1 = float(input('Insira sua nota: '))
nota2 = float(input('Insira sua nota: '))

nota_geral = (nota1 + nota2) / 2

if nota_geral >= 7 and nota_geral < 10:
    print('Aprovado')
elif nota_geral >= 10:
    print('Aprovado com Distinção')
else:
    print('Reprovado')
