# 10. Crie uma função que retorne uma lista com as pessoas cujo nome começa com a
# letra "J".

def pessoas_com_nome_j(pessoas):
    pessoas_com_j = []
    
    for pessoa_id, pessoa_info in pessoas.items():
        nome = pessoa_info['nome']
        
        if nome.startswith('J'):
            pessoas_com_j.append(pessoa_info)
    
    return pessoas_com_j

pessoas = {
    1: {'nome': 'João', 'idade': 25},
    2: {'nome': 'Maria', 'idade': 30},
    3: {'nome': 'Pedro', 'idade': 22},
    4: {'nome': 'Juliana', 'idade': 28}
}

pessoas_com_j = pessoas_com_nome_j(pessoas)
for pessoa in pessoas_com_j:
    print(f"Pessoa com nome começando com 'J': {pessoa['nome']}, {pessoa['idade']} anos")
