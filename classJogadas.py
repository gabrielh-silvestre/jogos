import random

# Variaveis
pedra = int(0)
papel = int(0)
tesoura = int(0)
jogadas = ["pedra", "papel", "tesoura"]

# conversor de jogada, transforma a str em in para o bloco if
player = str(input("Pedra, papel ou tesoura? "))
if player == "pedra":
    pedra += 1
elif player == "papel":
    papel += 1
elif player == "tesoura":
    tesoura += 1

# gerador de jogadas do bot
randomizer2 = random.randrange(0, 2)
bot = jogadas[randomizer2]
if bot == "pedra":
    pedra += 2
elif bot == "papel":
    papel += 2
elif bot == "tesoura":
    tesoura += 2

# bloco de resultados
if tesoura == 1 and papel == 2:
    print("Você ganhou")
elif tesoura == 1 and pedra == 2:
    print("Você perdeu")
elif papel == 1 and pedra == 2:
    print("Você ganhou")
elif papel == 1 and tesoura == 2:
    print("Você perdeu")
elif pedra == 1 and tesoura == 2:
    print("Você ganhou")
elif pedra == 1 and papel == 2:
    print("Você perdeu")
else:
    print("empate")

# aviso do resultado
print(f"Você jogou {player} e o oponente jogou {bot}")

#fazer condição de existencia
