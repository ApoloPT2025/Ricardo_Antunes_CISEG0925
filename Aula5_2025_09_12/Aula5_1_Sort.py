'''
Maneiras de sort
'''

#ListaNome=["Ricardo Antunes","Sonia Carina","Maria Russ","Ana Silva","Margarida Marques","Renato Gaspar"]
ListaNome=["Dario Almeida","Bruno Carvalho","Dario Quental"]
ListaNum=[5,1,4,8,3,9,7,6,2]
i=0
j=0
troca=True
controltroca=-1
il=1

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

while il<len(ListaNome):
#while troca: #Verifica se ha trocas. Loop controla as voltas da lista
    #troca=False #Flag control do loop se a troca
    i=0 #Reset do index na 1ra dimensao ( Nomes )
    print("OI")
    print("IL=",il)
    while i<len(ListaNome): #Loop controla a posição do nome
        print("Index pos=",i)
        #input()
        #troca=False
        if i<=len(ListaNome)-2:
            j=0 #Reset do index na 2da dimensao ( Letras )
            controltroca=-1
            #print(len(ListaNome[i]),"  -  ",len(ListaNome[i+1]))
            while j<len(ListaNome[i]) and j<len(ListaNome[i+1]): #Loop controla as letras
                if ord(ListaNome[i][j]) > ord(ListaNome[i+1][j]) and controltroca!=i:#Superior
                    print("If que troca i", i, "Depois da troca j",j)
                    print(ListaNome[i][j]," - ",ListaNome[i+1][j])
                    troca=True
                    controltroca=i #Controlo index da 1ra dimensao
                    print("Lista actual",ListaNome)
                    ListaNome.insert(i,ListaNome[i+1])#Atribui o valor do proximo index ao actual
                    ListaNome.pop(i+2)
                    print("Lista alterada",ListaNome)
                j+=1
        i+=1
    il+=1
    input()
