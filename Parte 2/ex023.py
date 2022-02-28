print("Calculadora de hipotenusa de um triângulo retângulo.")
co=float(input("Digite o cateto oposto:"))
ca=float(input("Digite o cateto adjacente:"))
hip=((co**2)+(ca**2))**(1/2)
print("Em um triângulo retângulo com catetos {} e {} a hipotenusa vale {}.".format(co,ca,hip))
#outra forma de fazer seria utilizando a função math.hypot(var1,var2) --> mais simples