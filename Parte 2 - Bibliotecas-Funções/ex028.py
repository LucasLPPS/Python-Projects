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
#frase.replace("X","Y") -> Irá procurar no texto a palavra X e substituir pela palavra Y
#frase.upper() -> Irá transformar as letras minúsculas em maíusculas
#frase.lower() -> Irá transformar as letras maíusculas em minúsculas
#frase.capitalized() -> Joga todas as letras para minúsculas e a primeira para maiúscula
#frase.title() -> Transforma toda letra de cada palavra contida na frase para minúscula e a primeira letra para maiúscula
#frase.strip() -> remove todas os espaços do início e final da frase (espaços inúteis)
#frase.rstrip() -> remove os espaços do final apenas
#frase.lstrip() -> remove os espaços do início apenas
#frase.split() -> Irá dividir a string por palavras, a contagem (posição da letra) irá reiniciar para cada palavra
#"X".join(frase) -> Irá substituir os espaços por "X" dentro da string
# essas são apenas algumas funções existentes, existem muito mais, ver na biblioteca no site oficial
frase="Lucas Pereira Pinheiro de Sousa"
print(frase[6:13]) # adicionar 1 na contagem de 12, pq o python ignora o último caractere
print(frase[:15:2])
print(frase.count("o"))
print(frase.upper().count("O"))
print(len(frase.strip())) # lembrar que posso combinar essas funções
frase2=frase.split()
print(frase2[0])
print(frase2[0][4]) # vai mostrar a primeira palavra do conjunto separado, e mostrar a 4º letra

