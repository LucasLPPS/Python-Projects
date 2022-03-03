#para importar toda a biblioteca = import math
#para importar apenas uma parte da biblioteca = Ex: from math import sqrt
#caso eu importe apenas uma parte específica, não há necessidade de escrever toda a setença
#Ex: math.sqrt(num) ficaria como sqrt(num)
import math
num=float(input("Digite um número para saber sua raiz quadrada:"))
raiz=math.sqrt(num)
print("A raiz quadrada de {} vale {:.2f}.".format(num,math.ceil(raiz)))#math.ceil(var) -- comando para arrendodar para cima
                                                                       #math.floor(var) -- comando para arredondar para baixo
                                                                       #todos esses comandos fazem parte da biblioteca math
# para ver as bibliotecas ir até o site do python!
# além das bibliotecas padrão, tbm existem os pacotes extras que podem ser importadas separadamente, e é alimentado pela comunidade
#para ver as bibliotecas externas vá em File -> Settings -> Project -> Python interpreter