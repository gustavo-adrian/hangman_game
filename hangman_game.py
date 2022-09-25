"""
Reglas:
-Incorpora comprehensions, manejo de errores y manejo de archivos.
-Utiliza el data.txt y léelo para obtener las palabras.

Ayudas y pistas:
-Investiga la función enumerate.
-El método get de los diccionarios puede servirte.
-La sentencia:
os.system("cls") -> Windows
os.system("clear") -> Unix 
te servira para limpiar pantalla.

Mejora el juego:
-Añade un sistema de puntos.
-Dibuja al "ahorcado" en cada jugada con código ASCII
-Mejora la interfaz
"""


import random
import os


def read_data():
    with open('./archivos/data.txt', 'r', encoding='utf-8') as f:
        list = [word for word in f]

        # elimino el salto de linea que figura como caracter
        words = []
        for word in list:
            word = ''.join(x for x in word if x not in '\n')
            words.append(word)

    return words


def word_choice():
    words = read_data()
    selected_word = random.choice(words)
    selected_word = list(selected_word)     # cada letra de la palabra la coloco en una lista
    guessed_word = '_'*len(selected_word)   # cada guion bajo representa una letra de la palabra 
    guessed_word = list(guessed_word)       # agrega cada guion bajo en una lista 

    return (selected_word, guessed_word) 

def accents(selected_word):
    selected_word_n = ''.join(selected_word).maketrans('áéíóú', 'aeiou')
    selected_word_n = ''.join(selected_word).translate(selected_word_n)  # esta es la variable que uso para comparar
    selected_word_n = list(selected_word_n)  # paso a lista
    
    return selected_word_n

def hangman():
    HANGMAN = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

    return HANGMAN

def hangman_game():
    selected_word, guessed_word = word_choice()
    selected_word_n =accents(selected_word)
    
    # mientras no se adivine la palabra se ejecuta el ciclo, comparo listas
    while selected_word_n != guessed_word:
        print('Adivina la palabra')
        # print(''.join(selected_word))   # transformo la lista en un string para mostrar al jugador
        print(' '.join(guessed_word))   # transformo la lista en un string para mostrar al jugador
        
        letter = input('Ingrese una letra: ').lower()

        # comparo la letra ingresada con cada elemento de la lista, que seria cada letra de la palabra seleccionada al azar, y reemplazo por indice en la lista donde se guardara la palabra adivinada

        HANGMAN = hangman()
        wrong_words = []
        for i, c in enumerate(selected_word_n):
            if c == letter:
                guessed_word[i] = c

            os.system ("cls")

    selected_word = ''.join(selected_word)
    print(f'¡Ganaste! La palabra es: {selected_word}.')


def run():
    hangman_game()


if __name__ == '__main__':
    os.system ("cls")
    run()
