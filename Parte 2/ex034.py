nome=str(input("Digite seu nome completo:")).strip()
separado=nome.split()
print("Primeiro nome: {}".format(separado[0]))
print("Ultimo nome: {}".format(separado[len(separado)-1]))# se eu usar a funçao len() para uma string que está separada,
                                                          # a leitura vai mudar de quantidade de letras para a quantidade
                                                          # de termos separados. Logo, eu tbm add -1, visto que a a posição
                                                          # em questão é sempre uma a menos do que a quantidade de termos
                                                          # Ex: [Ana, Maria, Sousa] -> posições [0,1,2] -> três termos