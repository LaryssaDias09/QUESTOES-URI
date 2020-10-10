matriz = []
soma = 0.0
indice = int(input())
operacao = input()
for i in range(12):
  linha = []
  for j in range(12):
    numero = float(input())
    linha.append(numero)
  matriz.append(linha)

for x in range(12):
  for y in range(12):
    if x == indice:
      soma+=matriz[x][y]

if operacao == "S":      
  print("%.1f"%soma)      
elif operacao == "M":
  print("%.1f"%(soma/12))
