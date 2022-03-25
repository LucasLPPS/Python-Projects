import numpy as np # posso chamar qualquer biblioteca de forma mais simples usando "as"

a = np.array([1, 2, 3, 4]) # para a criação de um array usando a biblioteca numpy: numpy.array(lista)
print(a)
print() # -------------------------------------------------------------------------------------------------------------
# -> quando eu crio um array utilizando numpy, a partir do momento que coloco mais de uma lista internamente, ele
#    já considera que a segunda lista declarada é a segunda linha de uma matriz de vetores
# -> para ser considerado uma matriz, fazer as duas listas internas a uma outra lista:
#    [[lista1], [lista2]] -> matriz
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(b)
print() # -------------------------------------------------------------------------------------------------------------
# -> para saber a dimensão do array, ou seja, quantas linhas tem a matriz, uso a função:
print(a.ndim) # matriz de uma linha (uma dimensão)
print(b.ndim) # matriz de duas linhas (duas dimensões)
print() # -------------------------------------------------------------------------------------------------------------
# -> para saber o formato do array, ou seja, quantas linhas e quantas colunas têm a matriz:
print(a.shape) # como só tem uma linha, vai retornar o número de colunas apenas
print(b.shape) # retorna (2, 4) -> duas linhas e 4 colunas
print() # -------------------------------------------------------------------------------------------------------------
# para criar um array (matriz) pré-determinada, com o tamanho que eu quiser:
c = np.arange(0, 11, 1)
# na função arange, eu uso 3 parâmetros: início, fim (lembrando que o último termo não conta), passo
print(c)
# se eu usar apenas um parâmetro, ele considera como o fim, onde o ínício é 0 e o passo é 1
d = np.arange(11)
print(d)
# se eu usar dois parâmetros, ele considera o início e fim, com passo 1
print() # -------------------------------------------------------------------------------------------------------------
# outra forma de criar um array é usando o linspace:
e = np.linspace(1, 10, 10) # obrigatoriamente devo ter 3 parâmetros: início, fim, quantos termos no intervalo
# nesse caso irá ser incluído o 10, caso eu não queira incluir: np.linspace(1, 10, 10, endpoint=False)
print(e)
# caso eu coloque 20 termos no intervalo, ele vai gerar de forma espaçada os 20 termos de 1 até 10
f = np.linspace(1, 10, 20)
print(f)
print() # -------------------------------------------------------------------------------------------------------------
# outra função, que facilita a criação de matrizes com poucos digitos:
g = np.ones((5, 5)) # -> considera como número de linhas e número de colunas. Caso eu coloque apenas um parâmetro,
                    #    considera como número de colunas, ou quantidade de termos
print(g)
# assim como o ones, tbm existe o zeros
print() # -------------------------------------------------------------------------------------------------------------
# outra função é a random, onde dentro dele existe a função rand, onde serão gerados números aleatórios entre 0 a 1
# -> os parâmetros indicam o número de linhas e colunas, caso seja digitado apenas um parâmetro, considera o número
#    colunas, ou termos
h = np.random.rand(5, 5)
print(h)
print() # -------------------------------------------------------------------------------------------------------------
# outra função que cria uma matriz identidade:
i = np.eye(4) # o parâmetro indica quantos termos 1 tem a matriz, logo, indica tbm o número de linhas e colunas
print(i)
# de forma semelhante, temos a função:
j = np.diag(np.array([1, 1, 1, 1])) # nesse caso ele irá criar uma matriz de zeros onde serão inseridos na sua diagonal
                                    # os termos indicados por mim
print(j)
print() # -------------------------------------------------------------------------------------------------------------
# de forma semelhante as litas, tbm posso acessar os elementos do array através dos indices
l = np.arange(10, 21)
print(l[0])
print(l[-1]) # último elemento
# para mais dimensões:
m = np.random.rand(5, 5)
print(m)
print(m[0]) # caso eu coloque apenas um parâmetro como índice, ele irá retornar a linha inteira referente aquele índice
print(m[0, 1]) # nesse caso irá retornar o elemento da linha 0 coluna 1
# tbm posso usar a estrutura m[0][1], que irá retornar a mesma resposta
# como é um array com o uso de listas, eu posso manipular e substituir os dados
m[0, 1] = 10
print(m)
print() # -------------------------------------------------------------------------------------------------------------
# tbm posso pegar fatias dos arrays criados:
n = np.arange(10, 21)
print(n[1:6]) # nesse caso irá retornar da posição 1 até a posição 5, já que a posição 6 não entra na contagem
# outras variações, da mesma forma que listas: n[:6] - da posição inicial até 5
#                                              n[1:] - da posição 1 até o final
#                                              n[:] - da posição incial até o final
#                                              n[1:6:2] - início, fim e passo
# para arrays com mais dimensões:
o = np.random.rand(3, 3)
print(o)
print(o[0:2]) # irá mostrar as duas primeiras linhas, lembando que a última linha não irá ser mostrada
# para pegar as colunas:
print(o[0:2, 2]) # irá mostrar apenas a coluna da posição 2 entre as linhas 0 e 2
print() # -------------------------------------------------------------------------------------------------------------
# operações entre arrays:
p = np.ones(10)
print(p)
print(p*10) # aqui entra os operadores: + - / * ** ....
np.random.seed(100) # sirão ser gerados abaixo números aleatórios uma vez apenas durante as próximas 100 execuções
q = np.random.randint(1, 20, 8) # irá retornar 8 números aleatórios entre 1 e 20
print(q)
r = np.random.randint(1, 20, 8)
print(r)
print(q*r) # -> aqui tbm entra os operadores comuns, tendo atenção para que o número de linhas e colunas das matrizes
           #    sejam iguais, caso não sejam, retornará erro
s = np.random.randint(1, 20, (3, 2)) # -> posso usar o shape no lugar do número de termos, nesse caso irá retornar uma
                                     #    uma matriz 3x2 com números aleatórios entre 1 e 20
t = np.random.randint(1, 20, (2, 3))
print(s.dot(t)) # -> nesse caso para multiplicar as duas matrizes assim como na matemática, usar a função dot
                #    que irá retornar uma matriz 3x3
print() # -------------------------------------------------------------------------------------------------------------
# para saber o tipo de dados da array:
print(t.dtype) # ira retornar que é do tipo inteiro
# para transformar o tipo:
print(t.astype('float'))
print(t.astype('str'))
# posso saber os valores mínimos e máximos:
print(t.min())
print(t.argmin()) # retorna a posição onde está o menor valor
print(t.max())
print(t.argmax())
print(t.mean()) # média dos valores
print(t.sum()) # soma dos valores
print(t.var()) # retorna a variância
print(t.std()) # retorna o desvio padrão
t.sort() # ordena os valores
print(t)
print(t[t % 2 ==0]) # outra forma de manipulação, irá retornar os valores positivos
print() # -------------------------------------------------------------------------------------------------------------






