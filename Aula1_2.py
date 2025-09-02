import time
#Aceder lista por 2 dimensoes

lst=["Gui","Pedro","Andorinha"]
lstindex=[]
i=0
j=0

while i<len(lst):
    j=0
    while j<len(lst[i]):
        print(i,"-",j) #Mostra o index
        print(lst[i][j]) #Mostra a letra
        j+=1
    i+=1

print("----------------------")

#Procurar

i=0
j=0
conta=0

print(lst)

nome=input("Name?\n")

while i<len(lst):
    j=0
    conta=0
    while j<len(lst[i]):
        print("J=",j)
        time.sleep(0.5)
        if j==len(nome):
            break
        if lst[i][j]==nome[j]:
            conta+=1
            print(lst[i][j],"-",nome[j])
            time.sleep(0.5)
        j+=1
        if conta==len(lst[i]):
            print("Found the name")
    i+=1

print("Contador",conta)






