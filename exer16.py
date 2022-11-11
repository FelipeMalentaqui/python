# Faça um programa que pergunte em que turno você estuda
# Peça para digitar M - Matutino || V - Vespertino || N noturno
# e imprima a mensagem Bom dia se for matutino, boa tarde se for vespertino ou boa noite se for noturno

from cgi import print_arguments
from os import system

system('cls')

turno = input('Em que turno você estuda? ')

if turno.lower() == 'matutino':
    print('Bom dia!')
elif turno.lower() == 'vespertino':
    print('Boa tarde!')
elif turno.lower() == 'noturno':
    print('Boa noite')
else:
    print('VOCÊ NÃO ESTUDA AQUI, SAI FORA!!')