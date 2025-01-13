salario = float(input("Digite o sálario do funcionário: "))

aumento = salario * 15 / 100

salario_aumento = salario + aumento

print ("O Sálario do funcionário é de: {:.2f} reais".format(salario))
print ("Com o aumento de 15% fica: {:.2f} reais".format(salario_aumento))