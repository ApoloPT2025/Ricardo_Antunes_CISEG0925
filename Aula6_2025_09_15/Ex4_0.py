'''
Exercicio 4 Ordena as Letras de Z-A de em uma lista com uma unica string.
        EX: lista=[" EU GOSTO E DO VERAO"]

Codigo ASCII letras maiusculas do 65 a 90
Codigo ASCII letras minusculas do 97 a 122

'''

lista=[" EU GOSTO E DO VERAO"]
lst=[]
i=0
j=0
temp=""

#for i in range(90,32,-1): #Ciclo para percorrer as letras de Z a A e espaço
for i in range(90,64,-1): #Ciclo para percorrer as letras de Z a A
    j=0
    while j<len(lista[0]): #Ciclo para percorrer cada letra na lista
        if i==ord(lista[0][j]): #Se encontrar letra, adiciona a uma nova lista
            temp=temp+chr(i)
        j+=1
lst.insert(0,temp)
print("A lista=",lista)
print("Ordenada de Z-A=",lst)
input()
