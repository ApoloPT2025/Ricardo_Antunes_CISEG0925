'''
Exercicio 4.1 Atualiza o codigo anterior para incluir letras pequenas e com acentos.
        Em que E maior , e menor ou é com acento valem o mesmo, e as restantes letras igual.
        Incluir todas as acentuações portuguesas a valer o mesmo que a letra normal tal como explicado em cima.
        EX: lista=[" Eu Gosto é do verão"]


Codigo ASCII letras maiusculas do 65 a 90
Codigo ASCII letras minusculas do 97 a 122
Codigo ASCII para espaço 32
'''

lista=[" Eu Gosto é do verão"]
lst=[]
i=0
j=0
temp=""

for i in range(255,31,-1): #Ciclo para percorrer a tabelas ASCII desde o espaço ate ao fim
    j=0
    while j<len(lista[0]): #Ciclo para percorrer cada letra na lista
        if i==ord(lista[0][j]): #Se encontrar letra, adiciona a uma nova lista
            temp=temp+chr(i)
        j+=1
lst.insert(0,temp)
print("A lista=",lista)
print("Ordenada de Z-A=",lst)
input()
