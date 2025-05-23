#Desafio extra

#Fazer a verificação ignorando acentuação

entrada = input("Digite uma palavra ou frase: ")

texto_limpo = ''.join(
    caractere.lower() for caractere in entrada
    if caractere.isalnum()
)

if texto_limpo == texto_limpo[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")