matriz=[]
for c in range(0,3):
    matriz.append(int(input(f"Digite o valor de [{0},{c}]:")))
for c in range(0,3):
    matriz.append(int(input(f"Digite o valor de [{1},{c}]:")))
for c in range(0,3):
    matriz.append(int(input(f"Digite o valor de [{2},{c}]:")))
print(f"[{matriz[0]}][{matriz[1]}][{matriz[2]}]"
      f"\n[{matriz[3]}][{matriz[4]}][{matriz[5]}]"
      f"\n[{matriz[6]}][{matriz[7]}][{matriz[8]}]")


