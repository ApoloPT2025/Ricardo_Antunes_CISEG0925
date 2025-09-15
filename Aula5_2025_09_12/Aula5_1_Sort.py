'''
Maneiras de sort
'''

ListaNome=["Ricardo Antunes","Sonia Carina","Maria Russ","Ana Silva","Margarida Marques","Renato Gaspar"]
ListaNum=[5,1,4,8,3,9,7,6,2]
i=0
j=0
aux=""
troca=True
controltroca=0

#Sort para numeros
'''
while troca:
    troca=False
    i=0
    while i<len(ListaNum):
        if i<=len(ListaNum)-2:
            if ListaNum[i]>ListaNum[i+1]:#Superior
                troca=True
                aux=ListaNum[i]#Armazera o valor no aux
                ListaNum[i]=ListaNum[i+1]#Atribui o valor do proximo index ao actual
                ListaNum[i+1]=aux#Coloca na proxima posiçao o valor no aux
        i+=1
print(ListaNum)
'''
while troca:#Verifica se ha trocas
    troca=False
    i=0
    while i<len(ListaNome):
        troca=False
        if i<len(ListaNome)-1:
            j=0
            print(len(ListaNome[i]),"  -  ",len(ListaNome[i+1]))
            while j<len(ListaNome[i]) and j<len(ListaNome[i+1]):
                if ord(ListaNome[i][j]) > ord(ListaNome[i+1][j]) and controltroca != i:#Superior
                    troca=True
                    controltroca=i
                    print("Lista actual",ListaNome)
                    ListaNome.insert(i,ListaNome[i+1])#Atribui o valor do proximo index ao actual
                    ListaNome.pop(i+2)
                    print("Lista alterada",ListaNome)
                    #break
                #input()
                j+=1
        i+=1
#print(ListaNome)
