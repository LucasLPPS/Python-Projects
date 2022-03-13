# import ex128_2.py # posso importar arquivos .py para que o que estiver nesse arquivo, seja adicionado no novo projeto
# -> todas as funções armazenadas em ex128_2 podem ser usadas agora.
# -> funciona da mesma forma que as funções importadas do próprio pycharm
# -> inclusive posso importar apenas uma das funções também:
# from ex128_2 import fatorial, dobro  -> retorna apenas essas duas funções
'''num = int(input("Digite um número:"))
fat = ex128_2.fatorial(num)
print(f"O fatorial de {num} é {fat}")
print(f"O dobro de {num} é {ex128_2.dobro(num)}")
print(f"O triplo de {num} é {ex128_2.triplo}")'''
# -> essa organizacção de códigos, separando o programa principal das funções, ou
# dividindo o programa em pequenas partes, chama-se modularização
# ---------------------------------------
# -> porém, mesmo com essa divisão de códigos, ainda assim, o arquivo que contém
# as funções pode ficar muito extenso, logo dentro desse mesmo arquivo, eu posso
# criar subdiviões, exemplo:
# Ex: ex128_2 vira um pacote; fatorial está dentro de uma subdivisão chamada "complexo"
#                         dobro e triplo estão dentro de uma subdivisão chamada "simples"
# -> o próprio usuário que cria essas subdivisões e escolhe quem fica dentro de quê.
# -> logo, para chamar um pacote específico:
# Ex: from ex128_2 import simples -> nesse caso só importará o pacote "simples", que
#                                    contém as funções dobro e triplo.
# -> a separação em pacotes acontece por meio de criação de pastas.
# -> crio um package principal "ex128_2", e dentro dele crio packages secundárias
#    "simples" e "complexo"
import Complexo
import Simples
num = int(input("Digite um número:"))
fat = Complexo.fatorial(num)
print(f"O fatorial de {num} é {fat}")
print(f"O dobro de {num} é {Simples.dobro(num)}")
print(f"O triplo de {num} é {Simples.triplo(num)}")
