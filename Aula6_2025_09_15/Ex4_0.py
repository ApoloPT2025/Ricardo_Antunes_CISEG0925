'''
Exercicio 4 Ordena as Letras de Z-A de em uma lista com uma unica string.
        EX: lista=[" EU GOSTO E DO VERAO"]

Codigo ASCII letras maiusculas do 65 a 90
Codigo ASCII letras minusculas do 97 a 122
'''

lista=["EU GOSTO E DO VERAO"]
lst=""
i=0
j=0
adiciona=0


for i in range(90,64,-1): #Ciclo para percorrer as letras de Z a A
    print(i)
    j=0
    while j<len(lista):
        print(f"J={j}, I={i}, Letra={chr(i)}")
        #print(lista[0][j])
        #print(ord(lista[0][j]))
        #input()
        if i==ord(lista[0][j]):
            print("Adicionado=",lista[0][j])
            adiciona+=1
            lst=lst+chr(i)
            print(lst)
            input()
        j+=1
print(lst)
input()





