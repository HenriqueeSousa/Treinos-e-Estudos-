dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos kilometros foram rodados? '))
pago = (dias * 60) + (km * 0.15)

print ('os total a pagar é de {:.2f}R$ '.format(pago))