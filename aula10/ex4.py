
import random
lista = input("digite uma lista de palavra separadas por espaço: ")
lista = lista.split(" ")
palavra = random.choice(lista).lower()
palavra_forca = ["_" for i in palavra]
chance = 0
print("A palavra é: ", end=" ")
print(" ".join(palavra_forca))
while palavra_forca.count("_") != 0 and chance != 6:
    letra = input("digite uma letra: ").lower()
    if letra in palavra_forca:
        print("Você ja usou essa letra antes, a palavra é:  ",
              " ".join(palavra_forca))
        continue
    if letra in palavra:
        for n in range(len(palavra)):
            if letra == palavra[n]:
                palavra_forca[n] = letra
        print("A palavra é: ", " ".join(palavra_forca))
        if "_" not in palavra_forca:
            print("\n\tParabéns! você acertou a palavra!\n")
        continue
    if letra not in palavra:
        chance += 1
        if chance == 6:
            print("Você errou pela 6 a vez.\n\n\tForca! Você perdeu! xP\n")
        else:
            print("voce errou pela ",
                  (chance), "a vez. Tente novamente")
