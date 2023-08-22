# 5. Crie uma função que remova uma pessoa do dicionário.

def remover_pessoa(nome_a_remover, dicionario):
    if nome_a_remover in dicionario:
        idade_removida = dicionario.pop(nome_a_remover)
        return idade_removida
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

nome_a_remover = input('Digite o nome a ser removido: ')
idade_removida = remover_pessoa(nome_a_remover, pessoas)
if isinstance(idade_removida, int):
    print(f"{nome_a_remover} foi removido com a idade de {idade_removida} anos.")
    print("Dicionário atualizado:", pessoas)
else:
    print(idade_removida)
