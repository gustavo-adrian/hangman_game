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
    with open('./files/data.txt', 'r', encoding='utf-8') as f:
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


def entry():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    while True:
        try:
            letter = input('Ingrese una letra: ').lower()
            if letter not in alphabet:
                raise Exception('Ingrese una letra. Intente de nuevo.')
            # if len(letter) > 1 or letter.isnumeric() or letter == '':
            #     raise Exception('Ingrese una letra. Intente de nuevo.')
            else:
                break
        except Exception as e:
            print(e)
            # os.system ("cls")
            
    return letter


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

    # si el usuario se equivoca 6 veces, pierde

    return HANGMAN


def hangman_game():
    selected_word, guessed_word = word_choice()
    selected_word_n =accents(selected_word)
    HANGMAN = hangman()
    words_used = []
    h = 0
    # mientras no se adivine la palabra se ejecuta el ciclo, comparo listas
    # while selected_word_n != guessed_word:
    while h < len(HANGMAN):
        print('Adivina la palabra') 
        print('Palabras usadas: ', '-'.join(words_used))
        print(HANGMAN[h])
        # print(''.join(selected_word))   # transformo la lista en un string para mostrar al jugador
        print(' '.join(guessed_word))   # transformo la lista en un string para mostrar al jugador
        
        letter = entry()
     
        # comparo la letra ingresada con cada elemento de la lista, que seria cada letra de la palabra seleccionada al azar, y reemplazo por indice en la lista donde se guardara la palabra adivinada

        words_used.append(letter)  
      
        if letter in selected_word_n:
            for i, c in enumerate(selected_word_n):
                if c == letter:
                    guessed_word[i] = c      
        else:
            h += 1
        os.system ("cls")

        if selected_word_n == guessed_word:
            break

    if h == len(HANGMAN): # el tamaño de la lista es 7, pero llega hasta el indice 6
        print(HANGMAN[h-1])
        print('¡Perdiste! La palabra era: ', ''.join(selected_word) )
    else:
        selected_word = ''.join(selected_word)
        print(f'¡Ganaste! La palabra es: {selected_word}.')


def run():
    hangman_game()


if __name__ == '__main__':
    os.system ("cls")
    run()
