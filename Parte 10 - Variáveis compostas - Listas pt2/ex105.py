matriz=[]
for c in range(0,3):
    matriz.append(int(input(f"Digite o valor de [{0},{c}]:")))
for c in range(0,3):
    matriz.append(int(input(f"Digite o valor de [{1},{c}]:")))
for c in range(0,3):
    matriz.append(int(input(f"Digite o valor de [{2},{c}]:")))
print("A sua matriz é:")
print(f"[{matriz[0]}][{matriz[1]}][{matriz[2]}]"
      f"\n[{matriz[3]}][{matriz[4]}][{matriz[5]}]"
      f"\n[{matriz[6]}][{matriz[7]}][{matriz[8]}]")
somapar=0
for c in matriz:
    if c%2==0:
        somapar=somapar+c
print(f"A soma dos números pares digitados é {somapar}.")
soma3coluna=matriz[2]+matriz[5]+matriz[8]
print(f"A soma da terceira coluna é {soma3coluna}.")
maior2linnha=0
if matriz[3]>=matriz[4]:
    maior2linha=matriz[3]
if matriz[3]>=matriz[5]:
    maior2linha=matriz[3]
if matriz[4]>=matriz[3]:
    maior2linha=matriz[4]
if matriz[4]>=matriz[5]:
    maior2linha=matriz[4]
if matriz[5]>=matriz[3]:
    maior2linha=matriz[5]
if matriz[5]>=matriz[4]:
    maior2linha=matriz[5]
print(f"O maior valor da 2º linha é {maior2linha}.")
'''Resolução do professor:
matriz=[[0,0,0],[0,0,0],[0,0,0]]
spar=mai=scol=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f"Digite o valor [{},{}]:"))
print("-="*30)
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end="")
        if matriz[l][c]%2==0:
            spar=spar+matriz[l][c]
    print() # para quebrar a linha
print("-="*30)
print(f"A soma dos valores par é {spar}.")
for l in range(0,3):
    scol=scol+matriz[l][2]
print(f"A soma dos valores da terceira coluna é {scol}.")
for c in range(0,3):
    if c==0:
        mai=matriz[1][c]
    elif matriz[1][c]:
        mai=matriz[1][c]
print(f"O maior valor da segunda linha é {mai}.")
'''

