a = int(input("Escolha a primeira letra: "))
b = int(input("Escolha a segunda letra: "))
c = int(input("Escolha a terceira letra: "))

delta = (b ** 2) - 4 * (a * c)
x1 = (-b + (delta ** 0.5)) / (2 * a)
x2 = (-b - (delta ** 0.5 )) / (2 * a)

if x1 == x2: {
    print("x = {}, delta={}".format(x1, x2, delta))
}
else: {
    print("x1 = {}, x2 = {}, delta={}".format(x1, x2, delta))
}