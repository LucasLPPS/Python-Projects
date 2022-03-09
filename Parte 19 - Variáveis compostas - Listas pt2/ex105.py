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

