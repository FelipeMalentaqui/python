""" Vamos trabalhar com dados de texto,
usando vairos metros, para verificar
o modificar o valor de uma variavel da class str """

# atalho: alt + shift + A

from cgi import print_arguments
from os import system

system('cls')

nomeCompleto = input('informe seu nome completo: ')

print(nomeCompleto)

# tamanho da minha string | Total de caracteres

print('1. total de caracteres: ', len(nomeCompleto))

#acessando um caracter apartir da posição

print('2. o caracter da posição 2 é:', nomeCompleto[2])

#transformando string em maiuscula | minuscula

print('3. texto em maiuscula', nomeCompleto.upper())
print('4. texto em minusculo', nomeCompleto.lower())
print('5. primeira letra maisculo', nomeCompleto.capitalize())

#procurar a posição de um determinado carctere 

print('6. posição do caractere espaço: ', nomeCompleto.find(' '))

# Fatiar uma string até uma determinada posição

espaco = nomeCompleto.find(' ')

print('7. somente o primeiro nome: ', nomeCompleto[0:espaco])

# substitur um caracter por outro

print('8. Nome sem espaço: ', nomeCompleto.replace('e', 'z'))

# Verificar somente letras ou letras e numeros

print('9. tem somente letras?', nomeCompleto.replace(' ', '').isalpha() )

print('10. É alfanumerico?', nomeCompleto.replace(' ', '').isalnum() )

#quebrar o texto em partes especificas retornando array

print('11. quebrar o trxto a cada espaço em brancos', nomeCompleto.split(' '))

# Centralizar o texto usando * para completar as laterais
print('12. centrealizar o texto entre * ')
print(nomeCompleto.center(80, '*'))


