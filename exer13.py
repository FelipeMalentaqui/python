#Faça um programa que receba 2 números e informe qual numero é maior

from os import system 
import random
system('cls')

numb1 = random.randint(0,100)
numb2 = random.randint(0,100)
numb3 = random.randint(0,100)

if numb1 > numb2 and numb1 > numb3:
    print(f'O numb1:{numb1} é maior que o numb2:{numb2} e numb3:{numb3}')
elif numb2 > numb1 and numb2 > numb3:
        print(f'O numb2:{numb2} é maior que o numb1:{numb1} e numb3:{numb3}')
else:
     print(f'O numb3:{numb3} é maior que o numb1:{numb1} e numb2:{numb2}')



