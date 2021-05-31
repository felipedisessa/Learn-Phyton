percorrido = float(input('quantos km foi percorrido?:'))
dias = float(input('quantos dias foi usado?:'))

pagar = (60 * dias) + (0.15 * percorrido)

print(f'Você utilizou o carro por {dias} dias e percorreu {percorrido} km. o valor total a pagar é de {pagar} reais')
