import math
cos = int(input("Adicione o cosseno em graus: "))
sin = int(input("Adicione o seno em graus: "))

if cos in [90, 270] and sin in [90, 270]:
    print("A tangente para este ângulo é indefinida (tende ao infinito)")
else:
    tan = (math.cos(math.radians(cos))) / (math.cos(math.radians(sin)))
    print(f"Tangente = {tan}")
#Mais uma vez eu perdi para a ia :(

angulo = int(input("Digite o ângulo em graus: "))

# Verifica múltiplos ímpares de 90°
if angulo % 180 == 90:
    print("A tangente para este ângulo é indefinida (tende ao infinito)")
else:
    tangente = math.tan(math.radians(angulo))
    print(f"Tangente = {tangente}")