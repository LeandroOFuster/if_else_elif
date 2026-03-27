gato = input("🐱 O gato está com fome? (Sim/Não): ")

if gato.strip().capitalize() == "Sim":
    print("🐱😋 O gato comeu o rato! 🐭💨")
elif gato.strip().capitalize() == "Não":
    print("🐱😴 O gato não comeu o rato! 🐭✅")
else:
    print("🐭💨 O rato fugiu do gato! 🐱😤")



