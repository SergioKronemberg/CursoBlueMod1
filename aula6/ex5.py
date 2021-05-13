def IMC(peso, altura):
    IMC = peso/(altura ** 2)
    print("o IMC é ={0:.2f}".format(IMC))


altura = float(
    (((input("qual altura?").replace(",", ".").lower()).replace("m", " ")).strip()))
peso = float((((input("qual seu peso?").replace(
    ",", ".").lower()).replace("kg", " ")).strip()))

IMC(peso, altura)

# se conseguir converter ok se nao printa inv
try:
    peso = float(peso)
    altura = float(altura)
    IMC(peso, altura)
except:
    print("invalido")
