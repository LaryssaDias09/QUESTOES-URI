x1,x2,x3,x4,x5,x6 = map(int, input(). split ())
y1,y2,y3,y4,y5,y6 = map(int, input(). split ())

pont = 0

if (x1 == y1 or x1 == y2 or x1 == y3 or x1 == y4 or x1 == y5 or x1 == y6):
    pont = pont + 1

if (x2 == y1 or x2 == y2 or x2 == y3 or x2 == y4 or x2 == y5 or x2 == y6):
    pont = pont + 1

if (x3 == y1 or x3 == y2 or x3 == y3 or x3 == y4 or x3 == y5 or x3 == y6):
    pont = pont + 1

if (x4 == y1 or x4 == y2 or x4 == y3 or x4 == y4 or x4 == y5 or x4 == y6):
    pont = pont + 1

if (x5 == y1 or x5 == y2 or x5 == y3 or x5 == y4 or x5 == y5 or x5 == y6):
    pont = pont + 1

if (x6 == y1 or x6 == y2 or x6 == y3 or x6 == y4 or x6 == y5 or x6 == y6):
    pont = pont + 1

if (pont == 3):
    print("terno")
elif (pont == 4):
    print("quadra")
elif (pont == 5):
    print("quina")
elif(pont == 6):
    print("sena")
else:
    print("azar")
