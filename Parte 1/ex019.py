temp=float(input("Digite a temperatura em ºC para converter:"))
k=temp+273
f=1.8*temp+32
print("A temperatura equivale a {}K(Kelvin) e {:.2f}F(Fahrenheit).".format(k,f))