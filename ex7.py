# 7. Crie uma função que retorne a média das idades das pessoas no dicionário.

def calcular_media_idades(pessoas):
    total_idades = 0
    total_pessoas = len(pessoas)
    
    for pessoa in pessoas.values():
        total_idades += pessoa['idade']
    
    if total_pessoas == 0:
        return 0  
    
    media_idades = total_idades / total_pessoas
    return media_idades

pessoas = {
    1: {'nome': 'João', 'idade': 25},
    2: {'nome': 'Maria', 'idade': 30},
    3: {'nome': 'Pedro', 'idade': 22}
}

media = calcular_media_idades(pessoas)
print(f"A média das idades é: {media:.2f}")
