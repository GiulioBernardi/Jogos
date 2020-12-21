import random
def jogar():

    global erro
    erros = (" _________\n""|        |\n""|         \n""|         \n""|         \n""|         \n""|           ", " _________\n""|        |\n""|        0\n""|         \n""|         \n""|         \n""|           ", " _________\n""|        |\n""|        0\n""|        !\n""|         \n""|         \n""|           ", " _________\n""|        |\n""|        0\n""|        !\n""|        ^\n""|         \n""|           ", " _________\n""|        |\n""|        0\n""|        !\\\n""|        ^\n""|         \n""|           ", " _________\n""|        |\n""|        0\n""|       /!\\\n""|        ^\n""|         \n""|           ", " _________\n""|        |\n""|        0\n""|       /!\\\n""|        ^\n""|         \\\n""|           ", " _________\n""|        |\n""|        0\n""|       /!\\\n""|        ^\n""|       / \\\n""|           ")
    print("Bem-vindo ao jogo de Forca!")
    print("Dificuldade: \n(1)Palavras de até 5 letras\n(2)Plarvas de até 7 letras\n(3)Palavras com até 10 letras")
    nivel = int(input("Escolha a dificuldade: "))
    easy = nivel == 1
    normal = nivel == 2
    hard = nivel == 3
    if(easy):
        palavra_facil = ("Copo", "Caixa", "Carro", "Livro", "Azul", "Globo", "Giz", "Mesa")
        palavra_gerada = random.choice(palavra_facil)
        #print(palavra_gerada.upper())
    elif(normal):
        palavra_normal = ("Lâmpada", "Caneca", "Alura", "Python", "Armario", "Espelho", "Chumbo")
        palavra_gerada = random.choice(palavra_normal)
        #print(palavra_gerada.upper())
    else:
        palavra_hard = ("Computador", "Governo", "Tecnologia", "Alimento", "Ventilador", "Programar", "Matemática")
        palavra_gerada = random.choice(palavra_hard)
        #print(palavra_gerada.upper())

    palavra_secreta = palavra_gerada.upper()
    letras_acertadas = []
    for letra in palavra_secreta:
        letras_acertadas.append('_')
    print(letras_acertadas)

    enforcou = False
    acertou = False
    index_limite = 0
    forca = 0

    while (not enforcou and not acertou):
        limite = len(palavra_gerada)

        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()

        index_palavra = 0  # contador
        for letra in palavra_secreta:  # letra = váriavel dentro da lista ["B", "a", "n", "a", "n", "a"]
            print("banana")
            erro = False
            if (chute == letra):
                letras_acertadas[index_palavra] = letra
            elif(chute not in palavra_secreta):
                erro = True
            index_palavra += 1
        if (erro == True):
            forca += 1
        print(erros[forca])
        print(letras_acertadas)
        index_limite += 1
        if(letras_acertadas.count('_') > 0):
            print("Faltam {} letras".format(str(letras_acertadas.count('_'))))
            if(forca == 7):
                print("\nVocê foi enforcado!")
                enforcou = True
        else:
            print("\nVocê concluiu o desafio! :D")
            acertou = True
if (__name__ == "__main__"):
    jogar()