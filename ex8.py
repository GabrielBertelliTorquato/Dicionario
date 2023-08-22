# 8. Crie uma função que retorne a pessoa mais velha do dicionário.

def pessoa_mais_velha(pessoas):
    pessoa_mais_velha = None
    idade_mais_velha = -1
    
    for pessoa_id, pessoa_info in pessoas.items():
        idade = pessoa_info['idade']
        
        if idade > idade_mais_velha:
            idade_mais_velha = idade
            pessoa_mais_velha = pessoa_info
    
    return pessoa_mais_velha

pessoas = {
    1: {'nome': 'João', 'idade': 25},
    2: {'nome': 'Maria', 'idade': 30},
    3: {'nome': 'Pedro', 'idade': 22}
}

pessoa_velha = pessoa_mais_velha(pessoas)
print(f"A pessoa mais velha é: {pessoa_velha['nome']}, {pessoa_velha['idade']} anos")
