from random import randint
from time import sleep
computador = randint(0,10)
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar')
print('-=-' * 20)
jogador = int(input("Em que numero eu pensei? "))
print("Processando...")
sleep(3)
if jogador == computador:
    print('Parabens!! Voce acertou...')
else: 
    print('Voce errou. Tente novamente!!')