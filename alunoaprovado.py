nome = input('qual seu nome?: ')
disciplina = input('qual o nome da disciplina?: ')
prova = float(input('qual a nota da sua prova?: '))
trabalho = float(input('qual a nota do seu trabalho prático?: '))
final = float(input('qual a nota do seu trabalho final?: '))

media = (prova + trabalho + final)/3
print(f' Sua média foi de {media:.2}')

if media >= 7:
    print('\033[1;32m Parabéns você foi aprovado!')
else:
    print('\033[1;31m infelizmente você não foi aprovado, pois não atingiu a média minima que é 7')
