# Atividade: Análise de Notas de uma Turma

# Solicita a quantidade de notas que serão informadas
quantidade = int(input("Quantas notas serão informadas: "))

# Cria uma lista vazia para armazenar as notas
notas = []

# Laço de repetição para receber as notas
for i in range(quantidade):

    # Solicita a nota de cada aluno
    nota = float(input(f"Digite a nota {i + 1}: "))

    # Adiciona a nota informada à lista
    notas.append(nota)

# Inicializa a variável que acumula a soma das notas
soma = 0

# Inicializa o contador de alunos aprovados
aprovado = 0

# Define a primeira nota como a maior nota inicial
maior_nota = notas[0]

# Define a primeira nota como a menor nota inicial
menor_nota = notas[0]

# Percorre todas as notas armazenadas na lista
for nota in notas:

    # Soma a nota atual ao total
    soma = soma + nota

    # Verifica se a nota é maior ou igual a 7
    if nota >= 7:

        # Incrementa o contador de aprovados
        aprovado += 1

    # Verifica se a nota atual é maior que a maior nota
    if nota > maior_nota:
        maior_nota = nota

    # Verifica se a nota atual é menor que a menor nota
    if nota < menor_nota:
        menor_nota = nota

# Calcula a média dividindo a soma pela quantidade de notas
media = soma / quantidade

# Exibe a média da turma com duas casas decimais
print(f"Média total: {media:.2f}")

# Exibe a quantidade de alunos aprovados
print(f"Quantidade de aprovados: {aprovado}")

# Exibe a maior nota da turma
print(f"Maior nota: {maior_nota:.2f}")

# Exibe a menor nota da turma
print(f"Menor nota: {menor_nota:.2f}")