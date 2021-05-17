l = "aeiou"
c = input("insira uma str: ")
vogal = 0
for i in c:
    if i in l:
        vogal += 1
print(f"tem {vogal} vogais")
