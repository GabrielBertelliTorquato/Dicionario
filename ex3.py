# 3. Crie uma função que receba um nome como parâmetro e retorne a idade da
# pessoa correspondente no dicionário.

def encontrar_idade_por_nome(nome, dicionario):
    if nome in dicionario:
        return dicionario[nome]
    else:
        return "Nome não encontrado no dicionário"

pessoas = {
    "João": 25,
    "Maria": 30,
    "Pedro": 28,
    "Ana": 22,
    "Carlos": 35,
    "Lúcia": 40,
    "Miguel": 19,
    "Sofia": 27,
    "Rafael": 32,
    "Laura": 24
}

nome_procurado = input('Digite o nome: ')
idade_encontrada = encontrar_idade_por_nome(nome_procurado, pessoas)
print(f"A idade de {nome_procurado} é {idade_encontrada} anos.")

