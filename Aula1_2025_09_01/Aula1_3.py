#Tabela ascii
import time

i=0
while i<258:
    time.sleep(0.1)
    print(i,"-",chr(i)) #Converte em caracter
    #print(ord(chr(i))) #Converte em inteiro
    i+=1