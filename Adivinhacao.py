import random
def jogar():

    print("Bem-vindo ao jogo de Adivinhação!")
    numero_secreto = random.randint(1, 100)
    pontos = 1000
    print("Nível de dificuldade:\n(1) 15 tentativas\n(2) 10 tentativas\n(3) 5 tentativas")
    nivel = int(input("Escolha o nível:"))
    easy = nivel == 1
    normal = nivel == 2
    hard = nivel == 3

    if(easy):
        qtd_chances = 15
    elif(normal):
        qtd_chances = 10
    elif(hard):
        qtd_chances = 5

    tentativa_atual = 1
    contador = qtd_chances
    while(tentativa_atual <= qtd_chances):
        ##print("Chance número: {}".format(tentativa_atual)) #string interpolation
        print("Tentativa {} de {}.".format(tentativa_atual, qtd_chances))  # string interpolation
        contador-=1
        tentativa_atual+=1
        tentativa = int(input("Digite um número de 1 a 100:"))
        if(tentativa >= 1 and tentativa <=100 ):
            acertou = tentativa == numero_secreto
            mais = tentativa > numero_secreto
            menos = tentativa < numero_secreto
            if(acertou):
                print("parabéns, você acertou o número")
                break
            else:
                print("Você errou! D: \n")
                if(mais):
                    print("Tente um número MENOR\n")
                elif(menos):
                    print("Tente um número MAIOR\n")
                    pontos_perdidos = abs(numero_secreto - tentativa)
                    pontos = pontos - pontos_perdidos
        else:
            print("BURRO")
            continue

    print("Você fez {} pontos!".format(pontos))
    print("O número era: {}".format(numero_secreto))

print("The end")

