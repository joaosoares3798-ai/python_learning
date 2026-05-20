print('Digite seu valor:')
value = input()

try:
    resultado = int(value)
except ValueError:
    try:
        resultado = float(value)
    except ValueError:
            resultado = value
print(type(resultado))