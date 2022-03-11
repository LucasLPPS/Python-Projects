def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mErro, digite um número inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("Entrada de dados interrompida pelo usuário.")
            return 0
        else:
            return n


num = leiaInt("Digite um valor:")
print(f"O valor digitado foi {num}")