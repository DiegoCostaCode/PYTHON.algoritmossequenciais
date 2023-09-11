print("CALCULADORA DE GASTOS - FRANGOTECH")

pe_direito = float (input ("digite o valor do chip direito: "))
pe_esquerdo = float (input ("digite o valor do chip esquerdo: "))

pe_esquerdo_calculo = pe_esquerdo * 2

valortotal = (pe_direito + pe_esquerdo_calculo)

print (f"O gasto total da granja é de {valortotal}")
