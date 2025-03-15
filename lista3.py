import math

def calcular_distancia(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Entrada dos pontos
x1 = float(input("Digite a coordenada x1: "))
y1 = float(input("Digite a coordenada y1: "))
x2 = float(input("Digite a coordenada x2: "))
y2 = float(input("Digite a coordenada y2: "))

# Cálculo e exibição da distância
distancia = calcular_distancia(x1, y1, x2, y2)
print(f"A distância entre os pontos ({x1}, {y1}) e ({x2}, {y2}) é: {distancia:.2f}")