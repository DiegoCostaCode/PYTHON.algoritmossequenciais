print ("DASHBOARD VOTOS")

voto_branco = float (input (" Qtd Voto branco:"))
voto_nulo = float (input ("Qtd Voto nulo:"))
voto_valido = float (input ("Qtd Voto válidos:"))

porcentagem_branco = voto_branco / 100 * 100
porcentagem_nulo = voto_nulo / 100 * 100
porcentagem_valido = voto_valido / 100 * 100

print (f"Os votos brancos representam {porcentagem_branco}% do total de votos.\n "
       f"Os votos nulos representam {porcentagem_nulo}% do total de votos. \n"
       f"Os votos validos representam {porcentagem_valido}% do total de votos.")
