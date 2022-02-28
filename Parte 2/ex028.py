#formas de fateamento:
#frase[X:Y] -> vai mostrar o texto da posição X à Y (Atenção que a contagem começa de zero)
#frase[X:Y:Z] -> vai mostrar da posição X até Y pulando de Z vezes
#frase[:X] -> vai mostrar a partir da posição 0 até X
#frase[X:] -> vai mostrar da posição X até o final da string
#frase[X::Y] -> vai mostrar da posição X até o final da string pulando de Y vezes
#len(frase) -> mostra a quantidade de caracteres
#frase.count("A") -> mostra a quantidade de letras "A" que tem no texto
#frase.count("A",X,Y) -> mostra a quantidade de letras "A" da posição X até Y
#frase.find("ABC") -> mostra quantas vezes foi encontrado no texto o conjunto de letras (juntas) "ABC"
#frase.find("D") -> caso não seja encontrado a letra, voltará como "-1"
#"ABC" in frase -> retorna true ou false, dizendo se tem ou não o termo na string

frase="Lucas Pereira Pinheiro de Sousa"
print(frase[6:13]) # adicionar 1 na contagem de 12, pq o python ignora o último caractere
