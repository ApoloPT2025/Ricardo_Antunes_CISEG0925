print("Aula 1, em 1 de Setembro de 2025")

#Variaveis
i=0
j=0
var1=0
listanome=["Gui","Pedro","Luis","Maria","Isabel","Ricardo","Sonia"] #Lista de varios tipos de dados
varletras="Hello World"

#Flags
flagigualdade=0
flagindex=[]

#Casting de str para int
var1=int(input("add a number"))

#Condição logica
if var1==2:
    print("happy new year")

print("----------------------")

#Ciclos de repetição for
for nome in listanome:
    print(nome)

print("----------------------")

#Ciclo de repetição while
while i<len(listanome):
    print(listanome[i])
    i+=1

print("----------------------")

#Add to list
listanome.append(input("Add name\n"))
print("----------------------")

#Remove from list
print(listanome)
listanome.remove(input("Name to remove\n"))
print("----------------------")
print(listanome)
listanome.pop(int(input("Index of name to remove\n")))
print("----------------------")
print(listanome)

nomeproc=input("name to search")
while j<len(listanome):
    if listanome[j]==nomeproc:
        flagigualdade+=1
        flagindex.append(j)
        #print("Name found")
    #else:
    #    print("Name not found")
    j+=1

if flagigualdade>0:
    print("Nomes encontrados nas posiçoes",flagindex)


















