print("Bem-vindo")
print("Esse script irá te auxiliar em exercícios com triângulos")
print("Basta forncer as suas medidas, que você receberá de volta se a classificação do triângulo!")

lados_triangulo = []

cont = 1
lado = 1
while(cont <= 3):
    entrada = int(input("Digite o {}º do triângulo: ".format(lado)))
    lados_triangulo.append(int(entrada))
    lado += 1
    cont += 1

for lado in lados_triangulo:
    reta_a = lados_triangulo[0]
    reta_b = lados_triangulo[1]
    reta_c = lados_triangulo[2]

