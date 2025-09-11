'''
Cria um programa que criptografe e descriptografe mensagens utilizando a tabela ASCII e uma chave String. A chave será uma palavra ou frase 
fornecida pelo utilizador, e a criptografia será feita com base na soma dos valores ASCII dos caracteres dessa chave.
Funcionamento da Criptografia
1.	O utilizador introduz:
    Uma mensagem (ex: "Olá Mundo")
	Uma chave em formato de string (ex: "chave")
2.	O programa:
	Calcula a chave numérica, somando os valores ASCII de cada letra da chave:
	"chave" → 'c'=99, 'h'=104, 'a'=97, 'v'=118, 'e'=101
Soma: 99 + 104 + 97 + 118 + 101 = **519**
	Usa essa soma (519) como valor para criptografar cada caractere da mensagem:
	'O' → ord('O') = 79 → 79 + 519 = 598
	'l' → ord('l') = 108 → 108 + 519 = 627
	etc.
3.	Para descriptografar, o programa deve subtrair o mesmo valor (519 neste caso) de cada número para recuperar os caracteres originais.
Requisitos:
1.	O programa deve conter três funções:
	criptografar(mensagem: str, chave: str) -> List[int]
	descriptografar(codigos: List[int], chave: str) -> str
	Listar
2.	Utilizar apenas funções nativas (ord() e chr()).
3.	Manter os espaços, acentos e distinguir entre maiúsculas e minúsculas.
4.	Impede que a chave seja vazia.
5.	Aplica rotação aos caracteres da mensagem encriptada (entre ASCII 32 e 126), para mantê-los dentro deste intervalo.
'''














