def tema_geografia():
    ##pega pergunta e resposta do banco de dados
    pass
def tema_historia():
    pass


def tema_cinema():
    pass


def tema_esportes():
    pass


def tema_tecnologia():
    pass


def tema_biologia():
    pass


def tema_matematica():
    pass


def tema_fisica():
    pass


def tema_todos():
    pass


def tema_aleatorio():
    pass


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
        tema_geografia()
    ##elif (historia):
    ##    tema_historia()
    ##elif (cinema):
    ##    tema_cinema()
    ##elif (esportes):
    ##    tema_esportes()
    ##elif (tecnologia):
    ##    tema_tecnologia()
    ##elif (biologia):
    ##    tema_biologia()
    ##elif (matematica):
    ##    tema_matematica()
    ##elif (fisica):
    ##    tema_fisica()
    ##elif (todos):
    ##    tema_todos()
    ##elif (aleatorio):
    ##    tema_aleatorio()
    else:
        print("Valor inválido!")

if(__name__ == "__main__"):
    jogar()

