preço = float(input('Digite o preço do produto: '))

desconto = preço * 5 / 100

preço_final = preço - desconto

print (f"O valor original do produto é de {preço} reais")
print (f"{preço} reais, com desconto de 5% fica : {preço_final} reais")
