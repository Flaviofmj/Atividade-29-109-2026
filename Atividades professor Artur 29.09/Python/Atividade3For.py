# Solicita um número ao usuário
numero = int(input("Digite um número e veja a tabuada de multiplicação: "))

# Laço de repetição que percorre os números de 1 até 10
for multiplica in range(1, 11):

    # Calcula o resultado da multiplicação
    resultado = numero * multiplica

    # Exibe a tabuada com o resultado
    print(f"{numero} x {multiplica} = {resultado}")