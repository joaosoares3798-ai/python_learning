import math

r = int(input("Digite seu alcance: "))
ang = int(input("Digite seu angulo em graus: "))

x = r * math.cos(math.radians(ang))
y = r * math.sin(math.radians(ang))

print(f"X: {x} Y: {y}")