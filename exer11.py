# Verifique se um número é par

number = input('informe um numero qulaquer: ')
number2 = input('informe outro valor para dividir')

divisao = int(number) / int(number2)

if divisao % 2 ==0:
    print(f'ele é um numero par, numero: {divisao}')
else:
    print(f'Ele é impar, numero {divisao}')
    