n1=int(input("Digite o primeiro número:"))
n2=int(input("Digite o segundo número:"))
s=n1+n2
m=n1*n2
d=n1/n2
e=n1**n2
print("A soma vale {}, a multiplicação {}, a divisão {:.3f}, e a exponenciação do primeiro pelo segundo {}".format(s,m,d,e))
                                            #{:.3f} significa dizer que eu quero 3 casas depois do ponto, com valores flutuantes
# coocar \n dentro do texto quebra a linha, e colocar ,end= continua a proxima linha na mesma linha atual