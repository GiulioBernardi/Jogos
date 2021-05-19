import forca
import Adivinhacao

print("Bem-vindo aos meus jogos")

valor_valido = True
while(valor_valido):

    print("Escolha seu jogo\n(1) Jogo de Forca\n(2) Jogo de Adivinhação")

    jogo = int(input("Escolha o jogo: "))

    if(jogo == 1):
        print("jogo de Forca\n")
        forca.jogar()
        valor_valido = False
    elif(jogo == 2):
        print("Jogo de Adivinhação\n")
        Adivinhacao.jogar()
        valor_valido = False
    else:
        print("Valor inválido\n")
        valor_valido = True