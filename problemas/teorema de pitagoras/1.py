import math
vel = float(input("Velocidade inicial em m/s: "))
ang = float(input("ângulo iniciais em graus: "))
gra = 9.81

vel = vel ** 2
resultado = vel * (math.sin(math.radians(2 * ang))) / gra
print(round(resultado, 2))
