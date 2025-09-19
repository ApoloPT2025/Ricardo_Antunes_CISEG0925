'''
Dicionarios sao nao ordenados e nao usam index mas sim mapping
Acesso a key : value em vez de index 0 1 2 3
type struct
mutaveis

'''

meudicionario={"nome": "Joao", "idade": 30}

print("Ler dicionario", meudicionario)

# Alterar valor
meudicionario["nome"]="Pedro"

print("Alterado valor de key nome", meudicionario)

for chave , valor in meudicionario.items():
    print(f"Key do dicionario ={chave} Valor = {valor}")

# Funçoes uteis
print("Items: ",meudicionario.items())
print("Keys: ",meudicionario.keys())
print("Values: ",meudicionario.values())
print("Get: ",meudicionario.get("nome"))
print("Get: ",meudicionario.get("mail")) #Se nao existir devolve None

meudicionario.update({"nome": "Antonio", "idade": 45})
print("Update items: ",meudicionario.items())
meudicionario["nomeproprio"]=meudicionario["nome"]
print("Items:",meudicionario.items())
del meudicionario["nome"]
print("Items:",meudicionario.items())

for chave , valor in meudicionario.items():
    print(f"Key do dicionario ={chave} Valor = {valor}")

