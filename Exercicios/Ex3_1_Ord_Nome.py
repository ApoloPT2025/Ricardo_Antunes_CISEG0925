listaNome=["Ricardo Antunes","Ana Santos","Sonia Carina","Antonio Magro","Maria Russ","Ana Silva","Margarida Marques","Andreia Torres","Ana Antunes","Renato Gaspar","Andreia Alves"]
#listaNome=["Dario Quental","Dario Almeida","Bruno Carvalho"]
# index         0               1                 2
#length 6
 
i=0
FlagTroca=True
it=0
controloTroca=-1 # guarda a posiçao da 1 dimensao(nome inteiro) que existiu uma troca
il=1
ordenado=0
 
 
while il<len(listaNome): #Loop controla as voltas a lista
    i=0 #Reposiçao do index da lista 1 dimensão ( Nome )
    #print("OI")
    #print("IL=",il)
    #print("Ordenado=",ordenado)
    #input()
    while i<len(listaNome) : #Loop controla a posiçao do nome
        print("Entrou dentro do loop I , pos=",i,"/",len(listaNome))
        #input()
        if i<=len(listaNome)-2:
            controloTroca=-1 #Reposiçao da variavel troca // tambem seria possivel usar um break
            it=0  #Reposiçao do index da lista 2 dimensão ( Letras )
            while it<len(listaNome[i]) and it<len(listaNome[i+1]): #Loop controla as letras no nome
                print("Entrou dentro do loop IT , pos=",it,"/",len(listaNome[i]))
                print(listaNome[i][it]," - ",listaNome[i+1][it])
                #input()
                if ord(listaNome[i][it])>ord(listaNome[i+1][it]) and controloTroca!=i: #Se letra > a proxima
                    print("I=",i,"I+1=",i+1)
                    print("Entrou dentro do if letra > proxima")
                    print(listaNome[i][it]," - ",listaNome[i+1][it]) #Print da letra com a proxima
                    print(listaNome) #Print da lista antes da troca
                    controloTroca=i #Controlar index da primeira dimençao ( quando acontece troca de nome ja nao é trocado nenhum nome)
                    listaNome.insert(i,listaNome[i+1])
                    #print(listaNome) #Print da lista quando muda o nome de lugar
                    listaNome.pop(i+2)
                    print(listaNome) #Print da lista depois da troca
                    #ordenado+=1
                    #print("Ordenado=",ordenado)
                    #it=0
                    #input()
                    break
                if ord(listaNome[i][it])<ord(listaNome[i+1][it]) and controloTroca!=i:
                    print("Inferior")
                    #input()
                    break
                #else:
                it+=1
                #break
            print("Saiu do loop IT")
            #input()
        i+=1
        print("Saiu do loop I")
        #input()
    il+=1
print(listaNome)
print("Fim")
input()
