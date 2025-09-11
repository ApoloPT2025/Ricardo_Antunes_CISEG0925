'''
Recebeste uma lista com nomes completos de várias pessoas. 
A tua tarefa é ordená-los alfabeticamente, considerando o primeiro nome como critério principal e o apelido como critério de desempate, 
com base nos valores ASCII dos caracteres.
Lista de Nomes:
nomes = [
    "Pedro Pereira",
    "Ana Beatriz",
    "Ana Clara",
    "Carlos Silva",
    "Beatriz Souza",
    "Ana Paula",
    "Pedro Andrade" ]
Regras:
1.	Ordena os nomes primeiro pelo primeiro nome comparando Caractere a Caractere.
2.	Se houver mais do que uma pessoa com o mesmo primeiro nome, usa o apelido como critério de desempate comparando Caractere a Caractere.
3.	Utiliza os valores ASCII implícitos na ordenação padrão de strings em Python (sem recorrer a bibliotecas).
Resultado Esperado:
Depois de ordenares, a lista deve ficar assim:
[
    "Ana Beatriz",
    "Ana Clara",
    "Ana Paula",
]

Codigo ASCII letras maiusculas do 65 a 90
Codigo ASCII letras minusculas do 97 a 122
'''
import time
lst=["Pedro Pereira","Ana Beatriz","Ana Clara","Carlos Silva","Beatriz Souza","Ana Paula","Pedro Andrade","Artur Coxo","Andreia Silva"]
i=0 #Variavel para while
j=0 #Variavel para while
ordenada=[] #Variavel para armazenar temporariamente a lista
letra=0 #Variavel para armazenar o numero ASCII da letra
inc=0 #Variavel para for
letra_maior=0

#Ordenar o primeiro nome
while j<3:
    if j==0:#Primeira letra
        for inc in range (65,91):#Letras maiusculas
            while i<len(lst):
                letra=ord(lst[i][j])#Armazena o numero em ASCII
                if inc==letra:
                    ordenada.append(lst[i])
                i+=1
            i=0
    else:#Restantes letras
        while i<len(lst):
            if i==0:
                ordenada.append(lst[0])#Vai guardar o primeiro nome da lista
                #print("Adicionado primeiro registo",ordenada)
                #time.sleep(1)
                #input()
            else:
                prim_letra=ord(lst[i][j-1])#ASCII primeira letra actual
                prim_letra_anterior=ord(ordenada[i-1][j-1])#ASCII primeira letra anterior
                print(f"Primeira letra={chr(prim_letra)}={prim_letra}, Primeira letra anterior={chr(prim_letra_anterior)}={prim_letra_anterior}")
                #input()
                if prim_letra_anterior<prim_letra: #Verifica se a letra anterior é superior a letra actual
                    letra_maior=1
                    print("Proxima primeira letra maior que a anterior")
                    print("Letra maior=",letra_maior)
                    #time.sleep(1)
                else:
                    letra_maior=0
                    print("Proxima primeira letra menor ou igual que a anterior")
                    print("Letra maior=",letra_maior)
                    #time.sleep(1)
                letra=ord(lst[i][j])
                if len(ordenada)==1:#Se a lista so tiver um registo
                    letra_anterior=ord(ordenada[0][j])
                else:#Se tiver mais registos
                    letra_anterior=ord(ordenada[i-1][j])
                if letra_anterior>letra and letra_maior==0:#Se letra anterior for superior e primeira letra for igual ou superior ao proxima
                    print(f"Letra anterior {letra_anterior} > a letra atual {letra}")
                    ordenada.insert(i-1,lst[i])
                    letra_maior=0
                if letra_anterior<letra:
                    print(f"Letra anterior {letra_anterior} < a letra atual {letra}")
                    ordenada.append(lst[i])
                if letra_anterior==letra:
                    print(f"Letra anterior {letra_anterior} = a letra atual {letra}")
                    ordenada.append(lst[i])
                if letra_maior==1:
                    print(f"Letra anterior {letra_anterior} > a letra atual {letra}")
                    ordenada.append(lst[i])
                    letra_maior=0
                print(ordenada)
                #time.sleep(5)
                input()
            i+=1
        i=0
    lst=ordenada
    ordenada=[]
    print("Lista=",lst)
    print("Ordenada=",ordenada)
    j+=1







