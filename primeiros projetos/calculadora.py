print('Qual conta você gostaria?')
print('1) Adicão')
print('2) Subtração')
print('3) Multiplicação')
print('4) Divisão')
conta = int(input('Escolha: '))
num1 = float(input('Numero 1: '))
num2 = float(input('Numero 2: '))
if conta == 1:
    resultado = num1 + num2
    operador = '+'
elif conta == 2:
    resultado = num1 - num2
    operador = '-'
elif conta == 3:
    resultado = num1 * num2
    operador = '×'
elif conta == 4:
    if num2 == 0:
        resultado = "IMPOSSIVEL DIVIDIR POR 0"
    else:
        resultado = num1 / num2
    operador = ':'
else:
    print('Invalido')


print(f"{num1} {operador} {num2} = {resultado}")

