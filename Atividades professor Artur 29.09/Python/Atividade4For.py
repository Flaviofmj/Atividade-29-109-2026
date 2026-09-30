# Pede a quantidade de alunos que serão cadastrados
quantidade_alunos = int(input("Digite a quantidade de alunos que serão cadastrados: "))

# Cria uma lista vazia para armazenar os alunos
alunos = []

# Cria contadores
maiores_idade = 0
aprovados = 0
reprovados = 0

# Cria variáveis para armazenar a maior e a menor nota
maior_nota = 0
menor_nota = 10

# Repete o cadastro conforme a quantidade informada
for i in range(quantidade_alunos):

    print(f"\nCadastro {i + 1}:")

    # Solicita os dados do aluno
    nome = input("Digite o nome: ")
    idade = int(input("Digite idade: "))
    curso = input("Digite o curso: ")
    nota = float(input("Digite a nota: "))

    # Guarda os dados do aluno em um dicionário
    aluno = {
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "nota": nota
    }

    # Adiciona o aluno na lista
    alunos.append(aluno)

    # Verifica se o aluno é maior de idade
    if idade >= 18:
        maiores_idade += 1

    # Verifica se o aluno foi aprovado ou reprovado
    if nota >= 6:
        aprovados += 1
    else:
        reprovados += 1

    # Verifica a maior nota
    if nota > maior_nota:
        maior_nota = nota

    # Verifica a menor nota
    if nota < menor_nota:
        menor_nota = nota


# Mostra os resultados
print("\n===== RESULTADO =====")
print("Quantidade de alunos cadastrados:", len(alunos))
print("Alunos maiores de idade:", maiores_idade)
print("Alunos aprovados:", aprovados)
print("Alunos reprovados:", reprovados)
print("Maior nota:", maior_nota)
print("Menor nota:", menor_nota)