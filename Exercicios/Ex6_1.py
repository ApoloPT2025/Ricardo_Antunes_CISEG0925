'''
Exercício 1: Criar um dicionário simples
Cria um dicionário chamado alunos que receba nome, idade e curso de cada aluno:
1-	Inserir
2-	Listar
O mesmo deve imprimir cada elemento do dicionário no seguinte formato por cada aluno:
Exemplo:
nome: Maria
idade: 20
curso: Engenharia
'''
import os

alunos={"nome": " ", "idade": " ", "curso": " "}

while True:
    os.system("cls")
    op=input("Qual opçao?\n1-Inserir\n2-Listar\n3-Sair\n")
    match op:
        case "1":
            os.system("cls")
            nome=input("Qual o nome?\n")
            idade=input("Qual a idade?\n")
            curso=input("Qual o curso?\n")
            alunos["nome"]=nome
            alunos["idade"]=idade
            alunos["curso"]=curso

            #input()
        case "2":
            os.system("cls")
            for n, i, c in alunos.items():
                print(f"O aluno {n}, com idade {i}, esta no curso {c}")
            input()
        case "3":
            os.system("cls")
            print("Adeus!")
            input()
            break
        case _:
            os.system("cls")
            print("Opção errada!")
            input()





