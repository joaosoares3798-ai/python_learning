import math

str = int(input("força em newtons: "))
ang = int(input("ângulo em graus: "))

str_x = str * math.cos(math.radians(ang))
str_y = str * math.sin(math.radians(ang))
print(str_x, str_y)