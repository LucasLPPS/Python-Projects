# Com as listas, posso personalizar (dar nomes) as posições de uma lista
# --------------------------------------
# para usar dicionários:
# dados=dict()
# dados={}
# ---------------------------------------
# supondo um exemplo para uma lista dados=("Pedro",25)
# para criar um dicionário, faço da seguinte forma:
# dados={"nome":"Pedro", "idade":25}
# estou atribuindo um nome a determinada posição da lista
# ---------------------------------------
dados={"nome":"Lucas","idade":29}
print(dados["nome"])
print(dados["idade"])
# ---------------------------------------
# não da para usar .append() com dicionários
# para adicionar um elemento a um dicionário usar: dados["sexo"]="M"
# para substituir um elemento de um dicionário usar: dados["idade"]=30
# estou atribuindo um novo elemento dentro do dicionário com o nome de "sexo"
# ---------------------------------------
# para deletar um dado do dicionário: del dados["idade"]
# ---------------------------------------
filme1={"título":"Star Wars","ano":1977,"diretor":"George lucas"}
# os elementos "título", "ano" e "diretor" são chamados no python de chaves(keys)
# há a possibilidade de acessar itens(tudo), chaves(nomes) ou valores
print(filme1.values()) # irá retornar os valores "Star Wars", 1977, "George Lucas"
print(filme1.keys()) # irá retornar os nomes "título", "ano", "diretor"
print(filme1.items()) # irá retornar tudo
# com isso posso usar laços para mostrar informações do dicionário:
for k,v in filme1.items(): # primeiro vem os Keys e depois os Values
    print(f"O {k} é {v}.")
# usar print(filme1[0]) irá retornar erro, pois não existe a posição 0, e sim a posição "título"
# ----------------------------------------
# posso misturar tuplas, listas e dicionários
locadora=list()
locadora.append(filme1)
filme2={"título":"Avengers","ano":2012,"diretor":"Joss Whedon"}
filme3={"título":"Matrix","ano":1999,"diretor":"Wachowski"}
locadora.append(filme2)
locadora.append(filme3)
print(locadora)
print(locadora[0]["título"])
print(locadora[1]["ano"])
print(locadora[2]["diretor"])
# ----------------------------------------
estado=dict()
brasil=list()
for c in range(0,3):
    estado["UF"]=str(input("Digite o estado:"))
    estado["sigla"]=str(input("Digite a sigla do estado:"))
    brasil.append(estado.copy()) # Não se deve usar brasil.append(estado) pois cria uma relação
                                 # e não se deve usar brasil.append(estado[:]) pois não se pode fatiar um dicionário
print(brasil)
for c in brasil: # para cada valor dentro da lista "brasil"
    for k,v in c.items(): # e para cada valor dentro do dicionário presente na respectiva posição da lista "brasil"
        print(f"O campo {k} tem valor {v}.")