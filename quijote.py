def clean_word(word):
    # Elimina caracteres de puntuación al principio y al final
    word = word.strip(".,;:!?\"'()[]{}*-#")
    
    # Convierte a minúscula
    word = word.lower()
    
    return word if word.isalpha() else ""

with open('Material Practicos/quijote.txt', 'r') as file:
    words_quijote = set(map(str, file.read().split()))

with open('Material Practicos/words_alpha.txt', 'r') as file:
    words_alpha = set(map(str, file.read().split()))    

print(f"Cantidad de palabras en Quijote: {len(words_quijote)}")
print(f"Cantidad de palabras en el diccionario: {len(words_alpha)}")

words_quijote_clean = set(clean_word(word) for word in words_quijote if clean_word(word))

words_alpha_clean = set(clean_word(word) for word in words_alpha if clean_word(word))

# Cantidad de palabras del libro que no existen en el diccionario
words_not_in_alpha = words_quijote_clean - words_alpha_clean

print(f"Cantidad de palabras en Quijote que no aparecen en el diccionario: {len(words_not_in_alpha)}")

# Ejemplos
print("Algunas palabras de Quijote que no aparecen en el diccionario:")
for word in sorted(words_not_in_alpha)[:20]: # solo las primeras 20 palabras para tener la terminal más limpia
    print(word)