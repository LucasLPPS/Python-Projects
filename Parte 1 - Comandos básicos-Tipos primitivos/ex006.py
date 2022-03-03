nome=input("Digite algo:")# como não estou delimitando nenhum tipo primitivo, sempre será string
print("O tipo primitivo é:",type(nome))
print("Só tem espaços?", nome.isspace())
print("Pode ser numérico?",nome.isnumeric())
print("Pode ser alfabético?",nome.isalpha())
print("Pode ser numérico e alfabético?",nome.isalnum())
print("Está em letras maíusculas?",nome.isupper())
print("Está em letras minúsculas?",nome.islower())
print("Está em letras maíusculas e minúsculas?",nome.istitle())#mistura de letras maíusculas e minúsculas
