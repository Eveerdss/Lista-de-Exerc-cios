# Contador de Vogais, Consoantes, Espaços e Outros Caracteres

frase = input("Digite uma palavra ou frase: ").lower()

vogais = "aeiou"
consoantes = "bcdfghjklmnpqrstvwxyz"

cont_vogais = 0
cont_consoantes = 0
cont_espacos = 0
cont_outros = 0

for caractere in frase:
    if caractere in vogais:
        cont_vogais += 1
    elif caractere in consoantes:
        cont_consoantes += 1
    elif caractere == " ":
        cont_espacos += 1
    else:
        cont_outros += 1

print("\nContagem de caracteres:")
print(f"Vogais: {cont_vogais}")
print(f"Consoantes: {cont_consoantes}")
print(f"Espaços: {cont_espacos}")
print(f"Outros caracteres: {cont_outros}")


