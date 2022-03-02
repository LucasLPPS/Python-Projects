# elif é um comando equivalente a else if, como forma de simplificar a utilização de if dentro de else
# lembrando que só deve ser utilizado dentro de if
nome=str(input("Digite seu nome:")).upper()
if nome=="LUCAS":
    print("Que nome bonito o seu!")
elif nome=="MARIA" or nome=="PEDRO" or nome=="PAULO":
    print("Seu nome é bem comum no Brasil")
else: # lembrando que esse else é opcional
    print("Seu nome é normal.")
print("Tenha um bom dia Sr(a). {}".format(nome.lower()))