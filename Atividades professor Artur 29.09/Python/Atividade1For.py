# Solicita uma frase e converte todas as letras para minúsculas
frase = input("Digite uma frase: ").lower()

# Define os caracteres que serão identificados
vogais = "aeiou"
espaco = " "
numero = "0123456789"
caractere = "!@#$%¨&*"

# Inicializa os contadores
contador_vogais = 0
contador_espaco = 0
contador_numero = 0
contador_caractere = 0

# Percorre cada caractere da frase
for i in frase:

    # Verifica se é uma vogal
    if i in vogais:
        contador_vogais += 1

    # Verifica se é um espaço
    if i in espaco:
        contador_espaco += 1

    # Verifica se é um número
    if i in numero:
        contador_numero += 1

    # Verifica se é um caractere especial
    if i in caractere:
        contador_caractere += 1

# Exibe os resultados
print("Quantidade de vogais:", contador_vogais)
print("Quantidade de espaços:", contador_espaco)
print("Quantidade de números:", contador_numero)
print("Quantidade de caracteres especiais:", contador_caractere)