# 4. Crie uma função que receba um nome e uma nova idade como parâmetros e
# atualize a idade da pessoa correspondente no dicionário.

def atualizar_idade(dicionario, nome, nova_idade):
    if nome in dicionario:
        dicionario[nome] = nova_idade
        print(f"Idade de {nome} atualizada para {nova_idade}")
    else:
        print(f"{nome} não encontrado no dicionário")

pessoas_idade = {'Gabriel': 20, 'Lucas': 20, 'Bruno': 22, 'Sid': 25, 'Serrano': 22, 'Bianca': 28, 'Ricardo': 25, 'Ronaldo': 30, 'Isak': 40, 'Jose': 21}

nome_atualizar = input("Digite o nome da pessoa que deseja atualizar a idade: ")
nova_idade = int(input("Digite a nova idade: "))

atualizar_idade(pessoas_idade, nome_atualizar, nova_idade)

print(pessoas_idade)


