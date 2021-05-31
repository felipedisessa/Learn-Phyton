print('''
Bem-vindo ao Banco do Pycharm
''')


saque = int(input('Qual será o valor a ser sacado? '))

valor = saque

nota = 50

total = 0

while True:
    if valor >= nota:
        valor -= nota
        total += 1
    else:
        if total > 0:
            print(f' O saque será realizado com {total} nota(s) de R${nota} ')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota= 5
        elif nota ==5:
            nota = 1
        total =0
        if valor == 0:


                print('Fim do programa, obrigado por utilizar')

                break





