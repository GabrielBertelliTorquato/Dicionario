# 2. Imprima o nome e a idade de todas as pessoas no dicionário.

pessoas_idade = {
    'Gabriel' :20, 
    'Lucas': 20, 
    'Bruno': 22, 
    'Sid' : 25, 
    'Serrano': 22, 
    'Bianca': 28, 
    'Ricardo': 25, 
    'Ronaldo':  30, 
    'Isak': 40, 
    'Jose': 21
    
}

for nome, idade in pessoas_idade.items():
    print(f"{nome} tem {idade} anos.")