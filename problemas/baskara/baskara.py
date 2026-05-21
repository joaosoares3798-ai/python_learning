print('Equação de 2 Grau:')

conta = str(input())

fatores = conta.split()

fator_a = fatores[0].replace("²", "").replace("^2", "")

if fator_a.isalpha():
    a = float(fator_a[0].lower().replace("x", "1"))
else: 
    a = float(fator_a[0].lower().replace("x", ""))

b = float('{}{}'.format(fatores[1], fatores[2]))

c = float('{}{}'.format(fatores[3], fatores[4]))

delta = (b ** 2) - 4 * (a * c)
x1 = (-b + (delta ** 0.5)) / (2 * a)
x2 = (-b - (delta ** 0.5 )) / (2 * a)

if x1 == x2: 
    print("x = {}, delta={}".format(x1, x2, delta))
else: 
    print("x1 = {}, x2 = {}, delta={}".format(x1, x2, delta))
