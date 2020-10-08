idadedia = int(input())

ano = idadedia // 365
idadedia = idadedia - ano*365

mes = idadedia // 30
idadedia = idadedia - mes * 30

dia = idadedia

print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(dia))
