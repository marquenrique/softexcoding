quantidade_Rodas = 4
peso_Bruto = 4500
quantidade_Pessoas = 8

if quantidade_Rodas == 2 or quantidade_Rodas == 3:
    print('CNH Categoria A')
elif quantidade_Rodas == 4 and quantidade_Pessoas == 8 and peso_Bruto<=3500:
    print('CNH Categoria B')
elif quantidade_Rodas >= 4 and peso_Bruto >= 3500 < 6000:
    print('CNH Categoria C')
elif quantidade_Rodas >= 4 and quantidade_Pessoas > 8:
    print('CNH Categoria D')
elif quantidade_Rodas >= 4 and peso_Bruto > 6000:
    print('CNH Categoria E')
else:
    print('Categoria não identificada')




