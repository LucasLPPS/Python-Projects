import math
print("Calculadora de seno, consseno e tangente de um ângulo.")
ang=float(input("Digite o ângulo:"))
sen=math.sin(math.radians(ang)) # a função math.randians converte o ângulo de graus para radianos
cos=math.cos(math.radians(ang)) # a função math.sin,.cos,.tan utiliza como base graus radianos
tan=math.tan(math.radians(ang))
print("Para o ângulo {:.2f}º, o seno vale {:.2f}, o cosseno {:.2f} e a tangente {:.2f}.".format(ang,sen,cos,tan))