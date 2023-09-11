produto = input ("digite o nome do produto: ")
print (produto)
valor = float (input ("digite o valor do produto: "))
print (valor)
desconto = float (input("digite o desconto a ser aplicado: "))
print (f"{desconto}%")

valor_desconto =  valor * (desconto/100)
valor_final= valor - valor_desconto
print(valor_final)
