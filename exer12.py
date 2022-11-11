from os import system 
import random 

system('cls')

# print(random.randint(0,200))

num1 = random.randint(0,100)

# O número escolhido é par ou impar?
# O número escohido é maior que 50 ou menor(mais perto do 100 ou do 0)
# O número escolhido é primo 

if num1 % 2 ==0:
    print(f'Este número é par: Número: {num1}')
else:
    print(f'Este número é impar: Número: {num1}')

if num1 > 50:
    print('Mais perto do 100')
else:
    print('Mais perto do 0')


