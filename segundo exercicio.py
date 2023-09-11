print ("contador de horas")

valor_inteiro = float (input ("Digite o valor: "))

horas = valor_inteiro // 3600
resto = valor_inteiro % 3600
minutos = resto // 60
segundos = resto % 60

print (f" Este valor correponde a {horas} horas e {minutos} minutos e {segundos}.")




