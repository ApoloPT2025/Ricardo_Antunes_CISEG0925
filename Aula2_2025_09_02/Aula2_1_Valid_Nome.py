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

#Validações
lst.append(input("What name?\n"))

while i<len(lst[0]):
    ch=ord(lst[0][i])
    if ch>=65 and ch<=90:#Verifica se é maiuscula
        maior+=1
    if ch>=97 and ch<=122:
        menor+=1
    if ch==32:
        maior=0
    i+=1

if maior==1 and menor>0:
    print("Nome válido")
    input()
else:
    print("Nome inválido: contem catacteres nao permitidos")
    input()