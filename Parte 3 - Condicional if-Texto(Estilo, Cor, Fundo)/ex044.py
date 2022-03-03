# cores no python -> \033[style;text;back m -> \033[0;33;44m
# style ->0 (none),1 (bold),4 (underline),7 (negative) - inverte
#text                background
#30      black       preto          40
#31      red         vermelho       41
#32      green       verde          42
#33      yellow      amarelo        43
#34      blue        azul           44
#35      Magenta     Magenta        45
#36      cyan        ciano          46
#37      grey        cinza          47
#97      white       branco        107
print("\033[4;31;45mOlá mundo\033[m")
print("\033[5;33;44mOlá mundo\033[m")
print("{}{}{}".format("\033[2;31;40m","Olá mundo","\033[m"))
cores={"amarelo": "\033[33m", "azul": "\033[34m"}
print("{}Olá mundo\033[m".format(cores["amarelo"]))
print("{}Olá mundo\033[m".format(cores["azul"]))
# existem várias formas de se colocar textos com cores, vai depender da forma
# e complexidade do meu código
