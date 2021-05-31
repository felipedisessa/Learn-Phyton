prices1 = (0, 600, 1200, 2000, 2500, 1300, 900, 0)

tupla1 = ('não existe', 'Stratocaster', 'telecaster', 'Les Paul', 'SG', 'Violão de aço', 'Violão de nylon', 0)


print('''
Bem vindo a nossa loja de instrumentos, você pode escolher seus produtos navegando por nosso sistema

Instrumentos de corda
[1] Stratocaster 
[2] telecaster
[3] Les Paul
[4] SG 
[5] Violão de aço
[6] Violão de nylon
[7] Passar de categoria

''')

pedido1 = int(input(' Qual instrumento você vai querer? '))

prices2 = (0, 100, 200, 1800, 0)

tupla2 = ('não existe', 'Flauta', 'Gaita', 'Saxofone', 0)

print('''
Instrumentos de sopro
[1] Flauta
[2] Gaita
[3] Saxofone
[4] Passar de categoria

''')

pedido2 = int(input('Qual instrumento você vai querer? '))

prices3 = (0, 2500, 200, 50, 0)

tupla3 = ('Não existe', 'Bateria', 'Cajón', 'Chocalho', 0)

print('''
Instrumentos de percussão
[1] Bateria
[2] Cajón
[3] Chocalho
[4] Finalizar pedidos

''')

pedido3 = int(input('Qual instrumento você vai querer? '))

end = (prices1[pedido1] + prices2[pedido2] + prices3[pedido3])
print(f'O valor final foi de {end} reais')

a = (prices1[pedido1])
b = (prices2[pedido2])
c = (prices3[pedido3])

if a >=1000:
    print(f'O produto da categoria de corda passou do valor de 1000 reais, com o preço de {prices1[pedido1]} reais')
if b >=1000:
    print(f'O produto da categoria de sopro passou do valor de 1000 reais, com o preço de {prices2[pedido2]} reais')
if c >=1000:
    print(f'O produto da categoria de percussão passou do valor de 1000 reais, com o preço de {prices3[pedido3]} reais')

if a < b and c:
    print(f'O produto mais barato foi de {a} reais e o produto foi: {tupla1[pedido1]},')
elif b < c and a:
    print(f'O produto mais barato foi de {b} reais e o produto foi: {tupla2[pedido2]}')
elif c < a and b:
    print(f'O produto mais barato foi de {c} reais e o produto foi: {tupla3[pedido3]}')



















