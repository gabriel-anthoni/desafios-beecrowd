# beecrowd | 1041 | Coordenadas de um Ponto
#
# Entrada:
#   - Leia uma string contendo dois números de ponto flutuante, X e Y.
#
# Lógica:
#   - Separe a string em 2 numeros de ponto flutuante para obter X e Y.
#   - Determine a localização do ponto no plano cartesiano:
#       1. Q1: X > 0 e Y > 0
#       2. Q2: X < 0 e Y > 0
#       3. Q3: X < 0 e Y < 0
#       4. Q4: X > 0 e Y < 0
#       5. Eixo Y: X = 0 e Y != 0
#       6. Eixo X: X != 0 e Y = 0
#       7. Origem: X = 0 e Y = 0
#
# Saída:
#   - Imprima a localização do ponto (quadrante ou eixo) ou "Origem".

# Código:
Coordinates = input().split()
x,y         = float(Coordinates[0]),float(Coordinates[1])
if   ( x > 0 ) and ( y > 0 ):
    print("Q1")
elif ( x < 0 ) and ( y > 0 ):
    print("Q2")
elif ( x < 0 ) and ( y < 0 ):
    print("Q3")
elif ( x > 0 ) and ( y < 0 ):
    print("Q4")
elif ( x == 0 ) and ( y != 0):
    print("Eixo Y")
elif ( x != 0 ) and ( y == 0):
    print("Eixo X")
else:
    print("Origem")