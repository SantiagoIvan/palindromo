sentence = input("Type a word or sentence: ")

def es_palindromo(palabra):
    palabra_procesada = sentence.replace(" ", "").lower()
    longitud = len(palabra_procesada)
    for i in range(round(longitud/2)):
        if (palabra_procesada[i] != palabra_procesada[longitud - i -1]):
            return False
    return True

def es_palindromo_v2(palabra):
    palabra_procesada = sentence.replace(" ", "").lower()
    return True if palabra_procesada[::]==palabra_procesada[::-1] else False
    

if es_palindromo_v2(sentence):
    print("The sentence is palindrome")
else:
    print("The sentence is not a palindrome")
