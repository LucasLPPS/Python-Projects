peso=float(input("Digite seu peso (Kg):"))
alt=float(input("Digite sua altura (m):"))
imc=peso/(alt*alt)
if imc<18.5:
    print("Você está abaixo do peso.")
elif imc>=18.5 and imc<25:
    print("Peso ideal.")
elif imc>=25 and imc<30:
    print("Você está em sobrepeso.")
elif imc>=30 and imc<40:
    print("Você está com obesidade.")
elif imc>=40:
    print("Você está com obesidade mórbida.")