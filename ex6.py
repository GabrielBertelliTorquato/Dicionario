# 6. Crie uma função que retorne a quantidade de pessoas no dicionário.

def contar_nome(dicionario):
    return len(dicionario)

dicionario = {
    'Gabriel': 25,
    'Lucas': 13,
    'Rafael': 15,
    'Letonia': 28
}

quantidade_nomes = contar_nome(dicionario)  # Chamando a função com o dicionário como argumento

print(f"Quantidade de nomes no dicionário: {quantidade_nomes}")
