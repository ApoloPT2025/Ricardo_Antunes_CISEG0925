'''
import re # Biblioteca REGEX

Validaçoes, substituições e procura de qualquer tipo de texto

"ABC" -----> Procura por padrao ABC no texto
[A-L] -----> Procura por qualquer valor dentro deste range de letras no texto
*.mp3 -----> Procura tudo o que acaba em .mp3 no texto

-- Funções

re.seach()   -----> Procura padrao em qualquer parte do texto
re.match()   -----> Procura do inicio da string
re.findall() -----> Devolve todas as ocorrencias
re.split()   -----> Divide a string em partes por padrao
'''

import re

texto="Hoje a aula acaba cedo demais as 18:15"

resultado=re.search(r"\d+",texto) # \d+ é para procurar em decimal, mas antes colocar a letra r de raw

print("-------Com opção - search---------")
print("Numero encontrado= ",resultado.group())
print("Na posição inicial",resultado.start())
print("Na posição final",resultado.end())
print("Span= ",resultado.span())
