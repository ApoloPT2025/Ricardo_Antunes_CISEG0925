'''
Declaraçao ()
Nao podem mudar nem adicionar depois de criados
Podem ser criados enquando o programa decorre

Mais comum utilizar em dicionarios dado que sao indexados tal como as listas
    Ex: String que nunca muda, extenções, parametros BD, keys de dicionario

    
'''

# Criar tuples
my_tuple_extentions=(".exe",".mp3",".docs",".jpg")
num1=0
num2=0

# my_tuple_extentions[0]=".mp4" # Nao pode fazer

print("Na segunda posiçao= ",my_tuple_extentions[1])

for ext in my_tuple_extentions:
    print(ext)


# Criar tuples in runtime
num1=int(input("Insert a number\n"))
num2=int(input("Insert a number\n"))

my_tuple_create=(num1,num2)

for extcreat in my_tuple_create:
    print(extcreat)

numero1, numero2= my_tuple_create

print(numero1)
print(numero2)


