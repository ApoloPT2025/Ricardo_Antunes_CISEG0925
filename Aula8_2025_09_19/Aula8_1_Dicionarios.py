''' Primeira parte

Pessoas={"Nome":"Ricardo","Telefone":914523578} #Dicionario de so uma pessoa
#Pessoas=[{"Nome":"Ricardo"},{"Nome":"Luis"}] #Lista de dicionarios

nome=input("Insere\n")
Pessoas.update({"Nome":nome}) #Adiciona caso nao existe o campo, se existir o nome do campo, actualiza
print(Pessoas.items())
print(Pessoas["Nome"])
print(Pessoas["Telefone"])
print(Pessoas.keys())
print(Pessoas.values())

for chave, valor in Pessoas.items():
    print(f"Key= {chave}, Valor= {valor}")

'''
Morada={"Rua":"Rua 6º Junho","Porta":[1,2,3,4,5,6,7,8,9]} #Dicionario com uma lista no interior

Morada["Porta"].pop(-1) #Apaga a ultima posiçao da rua

for chave, valor in Morada.items(): #Passa os campos Rua e Porta
    if isinstance(valor,list):
        for val in valor: #Passa os campos ventro da lista Porta
            print(f"{chave} : {val}")
    else:
        print(f"{chave} : {valor}")



