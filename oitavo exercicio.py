print ("calculador de aumento")

salario_base = float (input ("Digite o salario do colaborador: "))
aumento = float (input ("Digite a porcentagem de aumento: "))

valor_aumento = aumento * salario_base / 100
print (valor_aumento)

salario_final = salario_base + valor_aumento

print (f"O salario final deste colaborador será de {salario_final}")
