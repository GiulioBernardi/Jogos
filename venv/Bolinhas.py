from turtle import *
from freegames import *
from random import *

jogador = vector = (0, 0)
obstaculos = []

# MOVIMENTA O JOGADOR PARA CIMA
def click(x, y):
    subir = vector(0, 30)
    jogador.move(subir)


# VERIFICA SE OS ITENS ESTÃO NA TELA
def verifica_tela(itens):
    if (-200 < itens.x < 200 ) and (-200 < itens.y < 200):
        return True
    return False

# POSICIONA O JOGADOR NA TELA E VERIFICA SE ELE PERDEU.
def desenha(vivo):
    clear()
    goto(jogador.x, jogador.y)
    if vivo == True:
        dot(10, 'blue')
    else:
        dot(10, 'red')

    # VAI NA POSIÇÃO X,Y E DESENHA A BOLINA NA TELA
    # (X, Y SERÁ PASSADA NA FUNÇÃO move())
    for bolinha in obstaculos:
        goto(obstaculos.x, obstaculos.y)
        dot(20, 'black')
    update()

# MOVIMENTA OS ELEMENTOS NA TELA
def move():
    #gravidade:
    jogador.y -= 3

    # NUMS ALEATÓRIOS DE 0 A 10. BOLINHAS SÓ APARECEÇÃO SE O RETORNO FOR 0
    # ISSO PARA DIMINUIR A QTD DE BOLINHAS NA TELA
    if randrange(0, 10) == 0:
        # SPAWNA UMA BOLINHA NA TELA NO EIXO Y ENTRE -199 E 199
        bola = vector(199, randrange(-199, 199))
        obstaculos.append(bola)

    # MOVIMENTA OS OBSTÁCULOS PARA A ESQUERDA
    # DANDO A IMPRESSÃO DE MOVIMENTAÇÃO DO JOGADOR
    for bolinha in obstaculos:
        bolinha.x -= 3

    # ENQUANTO HOUVER ALGUMA BOLINHA NA LISTA DE OBSTÁCULOS (bolinhas na tela)
    # E A BOLA MAIS A ESQUERDA ESTIVER SAINDO DA TELA, ESTA SERÁ DELETADA
    # verifica_tela retorna false se a bolinha sair da tela
    # sendo assim,ele deleta a bolinha enquanto a bola estiver fora da tela
    while len(obstaculos) > 0 and not verifica_tela(obstaculos[0]):
        obstaculos.pop(0)

    # SE O JOGADOR FOR PRA FORA DA TELA, ELE PERDE O JOGO
    if not verifica_tela(jogador):
        desenha(vivo=False)
        return

    # SE O JOGADOR BATER NO OBSTÁCULO, ELE PERDE O JOGO
    for bolinhas in obstaculos:
        if bolinha - jogador < 15:
            desenha(vivo=False)
            return


