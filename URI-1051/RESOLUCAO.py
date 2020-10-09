sal = float(input())

if (sal <= 2000.00):
    print('Isento')
if (2000.00 < sal <= 3000.00):
    taxa8 = sal - 2000
    i = taxa8 * 0.08

if (3000.00 < sal <= 4500.00):
    taxa8 = 0.08 * 1000
    taxa18 = sal - 3000
    i = taxa18 * (18/100) + taxa8

if (sal > 4500):
    taxa8 = 0.08 * 1000
    taxa18 = 0.18 * 1500
    taxa28 = sal - 4500
    i = taxa18 + taxa8 + taxa28 * (28/100)

if (sal > 2000):
    i=float(i)
    print('R$ {:.2f}'.format(i))
