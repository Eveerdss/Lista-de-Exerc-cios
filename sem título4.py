# Gerador de Tabuada

numero = int(input("Você deseja ver a tabuada de qual número? "))

print(f"\nTabuada do {numero}:\n")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i:2} = {resultado}")

