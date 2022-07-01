def calculadora(n1, n2, operacao):
    if operacao == 'soma':
       return n1 + n2
    elif operacao == 'subtracao':
       return n1 - n2 
    elif operacao == 'multiplicacao':
       return n1 * n2 
    elif operacao == 'divisao':
      return  n1 / n2 
    else: return 0

print(calculadora(1,2,'soma'))