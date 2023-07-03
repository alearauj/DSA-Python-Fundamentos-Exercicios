# Projeto 1 - Desenvolvimento de Game em Linguagem Python

# Import
import random
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():

    # Para Windows
    if name == 'nt':
        _ = system('cls')

    # Para Mac ou Linux
    else:
        _ = system('clear')

# Função para jogo
def game():

    limpa_tela()

    print('\nBem-vindo(a) ao jogo da forca!')
    print('Adivinhe a palavra abaixo:\n')

    # Lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    # Escolhe randomicamente uma palavra
    palavra = random.choice(palavras)

    # List comprehension
    letras_descobertas = ['_' for letra in palavra]

    # Numeros de chances
    chances = 6

    # Letras erradas
    letras_erradas = []

    # Loop enquanto número de chances for maior do que 0
    while chances > 0:

        # Mostrar para o usuário
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        # Tentativas
        tentativa = input("\n Digite uma letra: ").lower()

        # Condicional
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        # Fim do jogo: usuário venceu
        if "_" not in letras_descobertas:
            print("\n Você venceu, a palavra era:",palavra)
            break

    # Fim do jogo: usuário perdeu
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era:", palavra)

# Bloco main: indica que esse script é um módulo python
if __name__ == "__main__":
    game()
    print("\nParabéns. Você está aprendendo programação em Python com a DSA. :)\n")