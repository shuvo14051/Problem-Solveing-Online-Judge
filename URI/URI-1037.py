N = float(input())

if ((N>=0.0) and (N<=25.0)):
    print("Intervalo [0,25]")

elif((N>25.0) and (N<=50.0)):
    print("Intervalo (25,50]")

elif((N>50.0) and (N<=75.0)):
    print("Intervalo (50,75]")

elif((N>75.0) and (N<=100.0)):
    print("Intervalo (75,100]")

elif((N<0.0) or (N>100.0)):
    print("Fora de intervalo")