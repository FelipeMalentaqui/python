num1 = input('Informe o valor 1: ')

divisor = input('informe valor div: ')

if num1.isalpha():
    print('Não é um número')

    
if int(divisor) > 0:
    print('posso dividir')
    divisao = int(num1) / int(divisor)
    print(f'resultado da divisao é {divisao}')
else:
    print('Valor 0 não pode ser dividido')


