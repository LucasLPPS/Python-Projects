try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a/b
except (ValueError, TypeError): # posso ter vários excepts
    print("Infelizmente tivemos um problema com os tipos que você digitou.") # isso vai aparecer quando houver um erro
except ZeroDivisionError:
    print("Não é possível dividir um número por zero.")
except KeyboardInterrupt:
    print("O usuário preferiu não informar nenhum dado.")
except Exception as erro: # irá mostrar qual foi o erro de forma geral
    print(f"O erro encontrado foi {erro.__cause__}.")
else:
    print(f"O resultado é {r}.")
finally: # isso vai aparecer independente de qualquer coisa
    print("Programa finalizado.")
# com essa estrutura, não aparecerá a mensagem de erro padrão do pycharm
