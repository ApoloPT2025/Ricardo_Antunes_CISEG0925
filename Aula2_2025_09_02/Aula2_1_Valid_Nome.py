'''
Cria um programa que peça ao utilizador para introduzir o seu nome completo. O programa deve validar se o nome contém apenas letras e espaços, a primeira letra do nome deve ser sempre maiúscula e a seguir ao espaço também, usando os códigos ASCII de cada caractere.
Exemplo:
Pedro Pereira 

Se o nome for válido, o programa deve exibir:
 "Nome válido!"
Caso contrário, deve exibir:
 "Nome inválido: contém caracteres não permitidos."
'''

i=0
lst=[]
maior=0
menor=0
ch=0
primeira=0
esp=0

#Validações
lst.append(input("What name?\n"))

while i<len(lst[0]):
    ch=ord(lst[0][i])
    if ch>=65 and ch<=90:#Verifica se é maiuscula
        if i==0:#Primeira letra
            primeira=1
        if esp>0 and maior==0:
            primeiro=1
        maior+=1
    if ch==32 and maior==1:
        primeira=0
        maior=0
        esp+=1
    i+=1
if primeira==1 and maior==1:
    print("Nome válido")
    input()
else:
    print("Nome inválido: contem catacteres nao permitidos")
    input()