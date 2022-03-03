n=input("Digite algo:")
print(type(n))
print("Pode ser numérico?",n.isnumeric()) # para casos onde eu queira descobrir se a string que coloquei é
print("Pode ser texto?", n.isalpha())# alfabética, numérica, etc, usar os comandos .is -- print(var.is...())
print("Pode ser texto/numérico?", n.isalnum())