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
'''
lst=["Pedro Pereira","Ana Beatriz","Ana Clara","Carlos Silva","Beatriz Souza","Ana Paula","Pedro Andrade"]
i=0
j=0
ordenada=[]
letra=0
maior=0

while i<len(lst):
    while j<3:#Loop ate 3ra letra
        letra=ord(lst[i][j])
        #print(f"Letra={lst[i][j]},asci={letra}")
        #input()
        if letra==65 or letra==97:
            print("Nome=",lst[i])
            print("Letra=",letra)
            input()
        if letra==32:
            break
        j+=1
    #print(i)
    i+=1
    j=0







