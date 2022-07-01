nome = input("Digite seu nome completo")
anoNascimento = int(input("Digite seu ano de nascimento"))

def suaIdade():
    try: 
        if anoNascimento >= 1922 and anoNascimento <= 2021:
            idadeAtual = 2022 - anoNascimento
            print(f"{nome} você completou ou completará {idadeAtual} anos em 2022")
    except Exception as erro:
        print("Ocorreu um erro! Digite um ano válido")
        while(erro == True):
            nome 
            anoNascimento
            suaIdade()