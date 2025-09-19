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

# Validar o mail

email="hoje.sexta_feira9@adeus.xau"

padrao=r"^[\w\.]+@[\w]+\.\w+$" # (^) -> inicio de string. (\w) -> todas as letras. (\.) -> caracteres especiais. ($) -> fim da string

resultado=re.match(padrao,email)

print(resultado.group())
print(resultado.start())
print(resultado.end())
print(resultado.span())

