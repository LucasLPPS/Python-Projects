def escreva(msg):
    espaço = len(msg.strip())
    print('~'*(espaço+4))
    print(f"  {msg}")
    print("~"*(espaço+4))


escreva("Lucas Pereira")
escreva("Teste")
escreva("Python")