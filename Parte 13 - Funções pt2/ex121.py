def contador(i, f, p): # para criar uma docstring, dentro da função use """explicação"""
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f"{c}", end=" ")
        c = c + p
    print("Fim.")


# para saber o que tem na explicação:
help(contador)
# uma docstring é um manual para a função
# ------------------------------------------
# supondo a seguinte função:


# original : def soma(a, b, c)
def soma(a=0, b=0, c=0):
    s = a + b + c
    print(f"A soma vale {s}")


soma(3, 2, 5) # a função nesse caso irá retornar sem erro
# -> mas se eu colocar soma(3, 2) irá retornar erro, pois falta um parametro, o "c"
# -> para contornar isso, colocar def soma(a, b, c=0), isso quer dizer, que se o
#    "c" não for informado, ele irá ser considerado 0, e não retornará erro.
soma(3, 2)
soma()
soma(c=3, a=1) # -> lembrando que pode ser feito fora de ordem, portanto que eu informe
               #     quem é cada variável
# ----------------------------------------------------


def teste():
  # n = 9 -> esse "n" irá ser considerado uma variável de escopo local, mesmo que
           # tenha a mesma nomenclatura do "n" global, mas existe uma forma de considerar
           # como sendo um novo valor para a variável global.
  # global n
  # n = 9 -> agora o programa irá entender que estou atribuindo o novo valor n para
           # escopo global
    x = 8
    print(f"Na função teste, n vale {n}")
    print(f"Na função teste, x vale {x}")


n = 2
print(f"No programa principal, n vale {n}")
teste()
# print(f"No programa principal, x vale {x}") -> irá dar erro, pois x é uma variável
                                            #   de escopo local, já n irá ser mostrado
                                            #   tbm na função, pois é uma variável de
                                            #   escopo global
# ---------------------------------------------------


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s # irá retornar no final o valor "s"


resp1 = somar(3, 2, 5)
resp2 = somar(2, 2)
resp3 = somar(2)
print(resp1, resp2, resp3)
# armazenando em variáveis utilizando o return me permite criar outras possibilidades de uso para as respostas
