# 1. Crie um dicionário aluno com as chaves "nome": "João", "idade": 18, "nota": 9.5. Imprima a idade
aluno = {"nome": "João", "idade": 18, "nota": 9.5} 
print("1. Idade do aluno:", aluno["idade"]) 

# 2. Adicione a chave "cidade": "São Paulo" no dicionário aluno. Imprima todas as chaves
aluno["cidade"] = "São Paulo" 
print("2. Chaves do dicionário:", aluno.keys()) 

# 3. Use um loop for para imprimir todas as chaves e valores do dicionário aluno.
print("\n3. Dados do aluno:")

for chave, valor in aluno.items(): 
    print(f"{chave}: {valor}") 

# 4. Crie um dicionário estoque com "maçã": 10, "banana": 5. Verifique se "laranja" existe (se não existir, adicione com valor 0).
estoque = {"maçã": 10, "banana": 5} 


if "laranja" not in estoque: 
    estoque["laranja"] = 0 
    
print("\n4. Estoque atualizado:", estoque)

# 5. Crie um dicionário agenda onde cada contato é outro dicionário (nome, telefone, email)
# Adicione 2 contatos e depois imprima o telefone do primeiro contato
agenda = {
    "contato1": {
        "nome": "Jurubeba", 
        "telefone": "99999-1111", 
        "email": "jurubeba@email.com"
    },
    "contato2": {
        "nome": "Jurupinga", 
        "telefone": "98888-2222", 
        "email": "jurupinga@email.com"
    }
} 
telefone_contato1 = agenda["contato1"]["telefone"] 
print(f"\n5. Telefone do primeiro contato: {telefone_contato1}") 