# 9. Crie uma função que retorne a pessoa mais nova do dicionário.

def pessoa_mais_nova(pessoas):
    pessoa_mais_nova = None
    idade_mais_nova = float('inf')
    
    for pessoa_id, pessoa_info in pessoas.items():
        idade = pessoa_info['idade']
        
        if idade < idade_mais_nova:
            idade_mais_nova = idade
            pessoa_mais_nova = pessoa_info
    
    return pessoa_mais_nova

pessoas = {
    1: {'nome': 'João', 'idade': 25},
    2: {'nome': 'Maria', 'idade': 30},
    3: {'nome': 'Pedro', 'idade': 22}
}

pessoa_nova = pessoa_mais_nova(pessoas)
print(f"A pessoa mais nova é: {pessoa_nova['nome']}, {pessoa_nova['idade']} anos")
