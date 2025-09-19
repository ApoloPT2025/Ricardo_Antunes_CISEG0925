'''
Files txt, json, csv    -> Criar persistencia
1º - carrregar o conteudo do ficheiro, open
2º - ações do ficheiro "Modo" /r (read), w (write), a (append), b ( binario), x, ... .
3º - fechar o ficheiro

open
read
close

programa

open
write // append
close
'''

filename="C:/Users/Admin/OneDrive - ATEC - Academia de Formação/2-CET 0925/UC00606 - Desenvolver programas em linguagem estruturada - 50h - Dario/Git/Ricardo_Antunes_CISEG0925/Aula7_2025_09_16/fname.txt"
frase=""

with open(filename,'r',encoding='utf-8') as manipfile:
    frase=manipfile.read()

print("Read ficheiro\n",frase)

frase=input("Escreva a frase\n")

print("\nA informaçao que vai adicionar ao ficheiro",frase)

with open(filename,'a',encoding='utf-8') as manipfile: #Faz append ao ficheiro
    manipfile.write(frase)
