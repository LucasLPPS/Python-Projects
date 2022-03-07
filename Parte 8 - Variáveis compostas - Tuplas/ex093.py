palavras=[]
while True:
    palavras.append(input("Digite uma palavra:").strip().upper())
    resp=str(input("Deseja cadastrar outra palavra? [S/N]:")).strip().upper()[0]
    while resp!="S" and resp!="N":
        print("Escolha uma opção válida!")
        resp=str(input("[S/N]:")).strip().upper()[0]
    if resp=="N":
        break
for termo in palavras:
    print(f"\nNa palavra {termo} temos ", end="")
    for letra in termo.lower():
        if letra in "aeiou": # checar, se dentro do termo específico existe um dos termos "aeiou"
            print(letra, end=" ")
