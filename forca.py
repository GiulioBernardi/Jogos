import random

def mensagem_dificuldade():
    print("Bem-vindo ao jogo de Forca!")
    print("Dificuldade: \n(1)Palavras de até 5 letras\n(2)Plarvas de até 7 letras\n(3)Palavras com até 10 letras")
def leitura_easy():
    txt = open("palavras_easy.txt", "r")
    palavra = []
    for linha in txt:
        linha = linha.strip()
        palavra.append(linha)
    txt.close()
    palavra_gerada = random.randrange(0, len(palavra))
    palavra_secreta = palavra[palavra_gerada].upper()
    return palavra_secreta
def leitura_normal():
    txt = open("palavras_normal.txt", "r")
    palavra = []
    for linha in txt:
        linha = linha.strip()
        palavra.append(linha)
    txt.close()
    palavra_gerada = random.randrange(0, len(palavra))
    palavra_secreta = palavra[palavra_gerada].upper()
    return palavra_secreta
def leitura_hard():
    txt = open("palavras_hard.txt", "r")
    palavra = []
    for linha in txt:
        linha = linha.strip()
        palavra.append(linha)
    txt.close()
    palavra_gerada = random.randrange(0, len(palavra))
    palavra_secreta = palavra[palavra_gerada].upper()
    return palavra_secreta
def quantidade_letras(palavra_secreta):
    return ['_' for letras in palavra_secreta]
def boneco_enforcado():
    return (" _________\n""|        |\n""|         \n""|         \n""|         \n""|         \n""|           ",
             " _________\n""|        |\n""|        0\n""|         \n""|         \n""|         \n""|           ",
             " _________\n""|        |\n""|        0\n""|        !\n""|         \n""|         \n""|           ",
             " _________\n""|        |\n""|        0\n""|        !\n""|        ^\n""|         \n""|           ",
             " _________\n""|        |\n""|        0\n""|        !\\\n""|        ^\n""|         \n""|           ",
             " _________\n""|        |\n""|        0\n""|       /!\\\n""|        ^\n""|         \n""|           ",
             " _________\n""|        |\n""|        0\n""|       /!\\\n""|        ^\n""|         \\\n""|           ",
             " _________\n""|        |\n""|        0\n""|       /!\\\n""|        ^\n""|       / \\\n""|           ")
def chute_usuario():
    chute = input("Digite uma letra: ")
    return chute.strip().upper()
def chute_correto(chute, letra, letras_acertadas,index_palavra):
    if (chute == letra):
        letras_acertadas[index_palavra] = letra
def imprime_boneco_e_letras(erros, forca, letras_acertadas):
    print(erros[forca])
    print(letras_acertadas)
def enforcado(palavra_secreta, enforcou):
    print("\nVocê foi enforcado!")
    print("A palavra era: ", palavra_secreta)
    enforcou = True
    return enforcou
def jogar():

    erros = boneco_enforcado()
    mensagem_dificuldade()
    nivel = int(input("Escolha a dificuldade: "))
    easy = nivel == 1
    normal = nivel == 2
    hard = nivel == 3

    if(easy):
        palavra_secreta = leitura_easy()
    elif(normal):
        palavra_secreta = leitura_normal()
    else:
        palavra_secreta = leitura_hard()

    letras_acertadas = quantidade_letras(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    index_limite = 0
    forca = 0

    while (not enforcou and not acertou):
        limite = len(palavra_secreta)
        chute = chute_usuario()
        index_palavra = 0

        for letra in palavra_secreta:
            erro = False
            if chute in palavra_secreta:
                chute_correto(chute, letra, letras_acertadas,index_palavra)
            else:
                erro = True
            index_palavra += 1

        if (erro == True):
            forca += 1

        imprime_boneco_e_letras(erros, forca, letras_acertadas)
        index_limite += 1

        if(letras_acertadas.count('_') > 0):
            print("Faltam {} letras".format(str(letras_acertadas.count('_'))))
            if(forca == 7):
                enforcou = enforcado(palavra_secreta, enforcou)
        else:
            print("\nVocê concluiu o desafio!! :D")
            acertou = True

if (__name__ == "__main__"):
    jogar()