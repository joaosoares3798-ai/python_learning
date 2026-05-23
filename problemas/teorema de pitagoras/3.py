import math
print(f"x: 0, {math.pi / 4}, {math.pi / 2}, {3 * math.pi / 4}, {math.pi}, {5 * math.pi}, {3 * math.pi / 2}, {7 * math.pi} {2 * math.pi} y = {math.sin(2 * math.pi)}")
#Essa versao nao esta totalmente errada o unico problema e que ela nao calcula apenas imprime

x = 0
passo = math.pi / 4

while x > 2 * math.pi:
    y = math.sin(x)
    print(f"{x:.2f} {y:.2f}")
    x += passo
# Essa e feita por ia