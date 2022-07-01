def mensagem_selecao():
    print("Lista de operações: 1: Soma  2: Subtração  3: Multiplicação  4: Divisão  0:  Sair")
 

operacao = ""

while (operacao != 0):
    mensagem_selecao()
    operacao = int(input("Digite o número para a operação correspondente"))
    if (operacao != 0, 1, 2, 3, 4):
        print("Essa opção não existe")
        mensagem_selecao()
        operacao
    num1 = int(input("Digite um valor"))
    num2 = int(input("Digite outro valor"))
    if operacao == 1:
        print("O resultado da sua soma é:" + num1 + num2)
        mensagem_selecao()
    elif operacao == 2:
        print("O resultado da sua subtração é:" + num1 - num2)
        mensagem_selecao()
    elif operacao == 3:
        print("O resultado da sua multiplicação é:" + num1 * num2)
        mensagem_selecao()
    elif operacao == 4: 
        print("O resultado da sua divisão é:" + num1 / num2)
    