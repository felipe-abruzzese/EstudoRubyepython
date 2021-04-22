#this is a guess the number game

import random

print('Ola, Qual e o seu nome?')
name = input()

print("Bem, " + name + "eu estou pensando em um numero entre 1 e 20, voce consegue adivinhar?")
secretNumber = random.randint(1,20)

for guessesTaken in range(1, 7):
    print("Chute um numero")
    guess = int(input())

    if guess < secretNumber:
        print("Seu chute foi muito baixo")
    elif guess > secretNumber:
        print("Seu chute foi muito alto")
    else:
        break #acertou!!

if guess == secretNumber:
    print('Bom Trabalho, ' + name + '! Voce acertou o numero em ' + str(guessesTaken) + ' tentativas.')
else:
    print('Nao, o numero que eu estava pensando era: ' + str(secretNumber))
