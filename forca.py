import random


def jogar():
    mensagem_abertura()
    # ------------------------------------------------------------------------------------------------------------------
    palavra_secreta = selecao_palavra_secreta()

    letras_acertos = inicializando_palavra_secreta(palavra_secreta)

    erros = 0
    enforcado = False
    venceu = False

    while not enforcado and not venceu:  # condição do game loop: não enforcou/perdeu e não ganhou
        print(letras_acertos)
        chute = input("Chute uma letra: ")
        chute = chute.lower().strip()

        if chute in palavra_secreta:
            visualizacao_acertos(palavra_secreta, chute, letras_acertos)
        else:
            erros += 1
            desenha_forca(erros)

        enforcado = erros == 7
        venceu = "_" not in letras_acertos

        mensagem_final(venceu, enforcado)
    print(f"A palavra era: {palavra_secreta}")


def mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def selecao_palavra_secreta():
    palavras_secretas = []  # criação da lista que armazenará as palavras lidas
    arquivo = open("palavras.txt", "r")  # leitura do arquivo que armazena as palavras

    for linha in arquivo:  # loop para adicionar as palavras lidas a lista
        linha = linha.strip()  # tratamento da string para retirar o \n
        palavras_secretas.append(linha)  # adição das palavras a lista
    arquivo.close()  # fechamento do arquivo

    numero = random.randrange(0, len(palavras_secretas))  # aleatorização do índice
    palavra_secreta = palavras_secretas[numero]  # escolha da palavra com base no índice

    return palavra_secreta


def inicializando_palavra_secreta(palavra_secreta):
    return ["_" for i in
            palavra_secreta]  # loop para adaptar a estrutura "oculta" ao tamanho da palavra secreta + lista criada afim de mostrar visualmente os acertos


def visualizacao_acertos(palavra_secreta, chute, letras_acertos):
    posicao = 0
    for letra in palavra_secreta:  # loop para verificar letra a letra
        if chute == letra:  # condicional que permite saber o posicionamento da letra chutada
            letras_acertos[posicao] = chute  # sobrescrição da lista com as letras nas posições corretas
        posicao += 1


def mensagem_final(venceu, enforcado):
    if venceu:
        print("Parabéns você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    elif enforcado:
        print("Que pena você foi enforcado.")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogar()
