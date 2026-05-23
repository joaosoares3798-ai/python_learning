#Isspace
texto1 = ' '
print(texto1.isspace())
#Saída: True

texto2 = 'ola mundo'
print(texto2.isspace())
#Saída: False

texto3 = ' \t\n '
print(texto3.isspace())
#Saída: True

texto4 = ''
print(texto4.isspace())
#Saída: False, precisa ter pelo menos um caractere

#Isnumeric
texto5 = '98'
print(texto5.isnumeric())
#Saída: True

texto6 = 'utugy83'
print(texto6.isnumeric())
#Saída: False

#Isalpha

texto7 = "olamundo"
print(texto7.isalpha())
#Saída: True

texto8 = "olamundo2"
print(texto8.isalpha())
#Saída: False

texto9 = "ola mundo"
print(texto9.isalpha())
#Saída: True

texto10 = "olá mundo"
print(texto10.isalpha())
#Saída: True

#Operadores aritimeticos

adicao = 5 + 5
subtracao = 5 - 5
multiplicacao = 5 * 5
divisao = 5 / 5
exponenciacao = 5 ** 5
#Divisao inteira
# e quantas vezes um numero cabe dentro de outro
# 10 // 5 = 2 * 5 = 2
divisao_inteira = 10 // 5
# resto, e bem explicativo e o resto da divisao:
resto = 15 % 4
print('adicao = {}, subtracao = {}, multiplicacao = {}, divisao = {}, exponenciacao = {}, divisao_inteira = {}, resto = {}'.format(adicao, subtracao, multiplicacao, divisao, exponenciacao, divisao_inteira, resto))