l = "aeiou"
c = input("insira uma str: ").lower()
frase = ""
for i in c:
    if i not in l:
        frase += i
print(frase)
