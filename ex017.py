import math
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = math.hypot(cateto_oposto,cateto_adjacente)

print ("O Comprimento da hipotenusa de um triângulo retângulo é {:.2f}".format(hipotenusa))

