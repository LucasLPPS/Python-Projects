expressão=str(input("Digite uma expressão matemática qualquer com parenteses:")).strip()
parenteses=list(expressão)
verificação=[]
for c in parenteses:
    if c=="(" or c==")":
        verificação.append(c)
if len(verificação)%2==0:
    print("Sua expressão está válida!")
else:
    print("Sua expressão não está válida!")