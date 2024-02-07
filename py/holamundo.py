word = input("ingrese una palabra")
word2 = input("ingrese otra palabra")

if len(word) >=3 and len(word2) >= 3:
    print((word and word2[-3:]))

elif len(word) >=2 and len(word2) >= 2:
    print((word and word2[-3:]))
else:
    print("esta opcion no es valida")
# elif word -[-3] == word2 -[-3]:
#     print("las palabras riman")

# elif word [-2] == word2 [-2]:
#     print("las palabras riman un poco ")

# else: 
#     print("las palabras no riman")