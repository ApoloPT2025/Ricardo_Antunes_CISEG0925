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

filename="C:/Users/Admin/OneDrive - ATEC - Academia de Formação/2-CET 0925/UC00606 - Desenvolver programas em linguagem estruturada - 50h - Dario/Git/Ricardo_Antunes_CISEG0925/Aula7_2025_09_16/fname_old.txt"
frase=""

#manipfile=open(filename,'w',encoding='utf-8') #A primeira vez para criar o ficheiro
manipfile=open(filename,'r',encoding='utf-8')
frase=manipfile.read()
manipfile.close()

print("Conteudo do ficheiro\n",frase)

frase=input("Escreva a frase\n")

print("\nA informaçao que vai adicionar ao ficheiro",frase)

manipfile=open(filename,'w',encoding='utf-8')
manipfile.write(frase)
manipfile.close()






