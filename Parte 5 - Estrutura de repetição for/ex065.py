# ir atrás de como tirar espaços, inverter um texto, colocar o
# nome das pastas com termos que identifiquem do que se trata, e commitar
# dizendo o que tá indo naquele commit, e mudar foto do perfil do github
frase=str(input("Digite alguma frase:")).upper()
frase2=frase.replace(" ","")
frase3=frase2[::-1] # forma de inverter um texto
print(frase3)
if frase2==frase3:
    print("Essa frase é um palíndromo.")
    print("{} == {}".format(frase2,frase3))
else:
    print("Esta frase não é um palídromo.")
    print("{} =/= {}".format(frase2, frase3))