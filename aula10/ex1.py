# Exercício 1 - Escreva um programa que pede a senha ao usuário,
#  e só sai do looping quando digitarem corretamente a senha.

senha = "xxx"
x = input('senha: ')
while x != senha:
    x = input('senha: ')
