# -> função tem como palavra chave rotina
# -> logo, se algo se repete constantemente no programa, ou no desenvolvimento
#    de diversos programas, posso criar uma função dessa rotina, diminuindo assim
#    o número de linhas usadas, e otimizando o tempo de desenvolvimento.
# -> para criar uma função:
def mostralinha():
    print("-"*30)


mostralinha()
print("Lucas") # -> entre a criação da função e o programa, deve haver 2 linhas
               #    vazias, o próprio pycharm sugere isso por questão estética.


def mensagem(msg): # -> posso misturar funções
    mostralinha()
    print(msg) #   -> o parametro é msg, que é o que vai ser substituído quando
    mostralinha() #   a função for chamada


mensagem("Lucas Pereira Pinheiro de Sousa")

# -> supondo uma repetição de uma soma:
# a=5
# b=8
# s=a+b
# print(s) -> s=13
# -> para não haver a necessidade de repetir toda vez que precisar efetuar a soma
#    desses dois números, posso criar a seguinte função:


def soma(a,b):
    print(f"A={a} e B={b}")
    s=a+b
    print(f"A soma de {a}+{b}={s}")


soma(5, 8) # -> caso eu coloque parametros a menos da função, ex: soma(5), irá
           #    retornar erro.
# -> posso tbm atribuir os valores diretamete na variável durante a chamada
#    da função, caso esteja vazio, irá considerar a ordem da criação da função
soma(a=8, b=5) # -> mas não posso fazer misturas, ex: soma(a=8, 5)


def contador(*num): # -> para casos em que eu não quiser limitar a quantidade de
    print(num)      #   de parametros, uso a expressão (* var)
    print(f"A quantidade números digitados foi de {len(num)}")
    s = 0
    for c in num:
        s = s + c
    print(f"A soma dos números é {s}.")


contador(3, 5, 6, 7, 8) # -> uma tupla


# -> criando uma função que dobra os valores digitados de uma lista (lista pode ser
#    modificada):
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] = lista[pos]*2
        pos = pos+1
    print(lista)


valores = [3, 5, 6, 7, 8]
dobra(valores)
