fruits = ['uva']

while True:
    print(f'Essa é a sua cesta: {fruits}')
    answer = input('''
    Você gostaria de adicionar algo?
    para adicionar responda ADD
    para remover responda R
     ''')
    if answer.lower() == 'add':
        add = input('O que gostaria? ')
        fruits.append(add)
        print(fruits)
    elif answer.lower() == 'r':
        delete = input('O que quer remover?')
        fruits.remove(delete)
        print(fruits)
    else:
        print('Digite uma opção válida ou feche o programa')







