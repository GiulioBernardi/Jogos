def jogar():
    print("Bem-vindo ao meu QUIZ")
    print("Escolha uma opção de tema\n(1)Geografia\n(2)História\n(3)Cinema\n(4)Esportes\n(5)Tecnologia\n(6)Biologia\n(7)Matemática\n(8)Física\n(9)Todos\n(10)Aleatório")
    tema = int(input("Escolha o tema: "))

    geografia = tema == 1
    historia = tema == 2
    cinema = tema == 3
    esportes = tema == 4
    tecnologia = tema == 5
    biologia = tema == 6
    matematica = tema == 7
    fisica = tema == 8
    todos = tema == 9
    aleatorio = tema == 10

    if (geografia):
        pass
    elif (historia):
        pass
    elif (cinema):
        pass
    elif (esportes):
        pass
    elif (tecnologia):
        pass
    elif (biologia):
        pass
    elif (matematica):
        pass
    elif (fisica):
        pass
    elif (todos):
        pass
    elif (aleatorio):
        pass
    else:
        print("Valor inválido!")

if(__name__ == "__main__"):
    jogar()

