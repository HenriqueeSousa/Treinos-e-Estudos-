valor = float(input('Digite quanto você tem na carteira: '))
dolar = 6.157

carteira = valor / dolar

print ('você possui: {} reais em sua carteia, e consegue comprar {:.3f},em dolar'.format(valor,carteira))