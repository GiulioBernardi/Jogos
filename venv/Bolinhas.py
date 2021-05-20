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
    if (-200 < itens.x < 200 ) and (-200 < itens.x < 200):
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
    #pinta os obstáculos de preto
    for bolinha in obstaculos:
        goto(obstaculos.x, obstaculos.y)
        dot(20, 'black')
    update()

# CRIA O EFEITO DE GRAVIDADE
def move():
    #gravidade:
    jogador.y -= 3

    # NUMS ALEATÓRIOS DE 0 A 10. BOLINHAS SÓ APARECEÇÃO SE O RETORNO FOR 0
    # ISSO PARA DIMINUIR A QTD DE BOLINHAS NA TELA
    if randrange(0, 10) == 0:
        # SPAWNA UMA BOLINHA NA TELA NO EIXO Y ENTRE -199 E 199
        bola = vector(199, randrange(-199, 199))
        obstaculos.append(bola)