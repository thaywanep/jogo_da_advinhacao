#Jogo Da Advinhação
from random import randint
from time import sleep
import emoji

numero_sorteado = randint(1, 100) #Faz O Computador "PENSAR/ESCOLHER"
print('=*=' * 20)

#Introdução

print(emoji.emojize('Olá, Sou InteligenThay uma Inteligência Artificial :smiling_face_with_open_hands:'))
sleep(1)
print(emoji.emojize('Vamos jogar o Jogo Da Advinhação! :beaming_face_with_smiling_eyes:'))
sleep(1)
print('Eu vou pensar em um número entre 1 e 100.\n'
      'E você terá 10 tentativas para advinhar qual o número em que pensei.')
sleep(1)
print('Mas calma eu te darei umas dicas se seu chute está baixo ou alto...')
sleep(1)
print(emoji.emojize('Se você conseguir acertar antes que as 10 vidas acabe você me vence! :flexed_biceps: '))
print('=*=' * 20)
jogador = input('Qual o seu nome? ')
print('Vamos começar {}! Está preparado? '.format(jogador))
sleep(1)
print('=*=' * 20)
print(emoji.emojize('Vou pensar em um número de 1 a 100. :thinking_face: Tente advinhar...'))
print('=*=' * 20)
sleep(1)

#Início Jogo
palpites = int(10)
numero_escolhido = int(input('Em que número pensei? ')) #Jogador Tenta Advinhar
print('PROCESSANDO...')
sleep(2)

#Início Loop
while palpites >= 0:   #Jogador Não Tem Mais Vidas
    if numero_escolhido != numero_sorteado and palpites == 1:
        print(emoji.emojize('\033[32mGANHEI! {}, Suas vidas acabaram.\n\033[m'
                            '\033[32mEu pensei no número {}! :smiling_face_with_sunglasses: \033[m'.format(jogador, numero_sorteado)))
        break

    elif numero_escolhido != numero_sorteado and palpites > 1:  #Jogador Errou Mas Ainda Tem Vidas
        palpites = palpites - 1
        print('\033[31mVocê errou o número, perdeu 1 vida...\033[m')
        print('\033[31mVocê ainda tem {} vidas.\033[m'.format(palpites))
        if numero_escolhido > numero_sorteado:
            print('\033[33mFoi um chute alto {}, tente um número menor...\033[m' .format(jogador))
        elif numero_escolhido < numero_sorteado:
            print('\033[33mFoi um chute baixo {}, tente um número maior...\033[m' .format(jogador))

        numero_escolhido = int(input('Em que número pensei?'))  #Jogador Tenta Advinhar
        print('PROCESSANDO...')
        sleep(2)

    else: #Jogador Acertou
        print(emoji.emojize('\033[32mPARABÉNS {}!!! Você conseguiu me vencer :partying_face:! \n\033[m'
                            '\033[32mEu pensei no número {}!\033[m'.format(jogador, numero_sorteado)))
        break


#Fim De Jogo :)
