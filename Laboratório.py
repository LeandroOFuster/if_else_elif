temperatura = float(input("Digite a temperatura em C°: "))
if temperatura <= 0:
    print("Temperatura abaixo de zero! Cuidado com o congelamento. ")
elif temperatura <= 15:
    print("Frio intenso no laboratório.")
elif temperatura <= 25:
    print("Temperatura agradável no laboratório.")
else:
    print("Temperatura alta no laboratório! Verifique o sistema de refrigeração.")