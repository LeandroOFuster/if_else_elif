idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

temperatura = float(input("Digite a temperatura en C°:"))
if temperatura > 30:
    print("Está quentee!")
elif temperatura > 20:
    print("Está agradável!")

valor_compra = float(input("Digite o valor da compra: "))
if valor_compra > 100:
    print("Você ganhou um desconto de 10% ")
else:
    print("Você não ganhou desconto. ")

nota = float(input("Digite sua nota Final: "))
if nota >= 9:
    print("Excelente desempenho.")
elif nota >= 7:
    print("Aprovado!")
elif nota >= 5:
    print("Recuperação.")
else:
    print("Reprovado")
    