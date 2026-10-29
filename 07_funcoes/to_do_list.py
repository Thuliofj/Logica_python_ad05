from cores import *

tarefas = []

def menu():
    print(FRENTE_AMARELO + "___MENU___" + RESET)
    print(FRENTE_MAGENTA + "1 - Adicionar Tarefa" + RESET)
    print(FRENTE_MAGENTA + "2 - Listar Tarefa" + RESET)
    print(FRENTE_MAGENTA + "3 - Remover Tarefa" + RESET)
    print(FRENTE_MAGENTA + "4 - Sair" + RESET)

def adicionarTarefa():
    tarefa = input("Digite o nome da tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa Adicionada!")

def ListarTarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada")
    else:
        for numero, tarefa in enumerate(tarefas, start=1):
            print (numero, "-", tarefa)

def removerTarefa():
    ListarTarefas()
    
    if len(tarefas) > 0:
        numero = int(input("Digite o numero da tarefa a remover:"))

        if 1 <= numero <= len(tarefas):
            tarefas.pop(numero -1)
            print("Tarefa Removida!")
        else:
            print("Numero Inválido")

opcao = ""

while opcao != "4":
    menu()
    opcao = input("Escolha uma opção:")

    if opcao == "1":
        adicionarTarefa()
    elif opcao == "2":
        ListarTarefas()
    elif opcao == "3":
        removerTarefa()
    elif opcao == "4":
        print("Até Logo!")
    else:
        print("Opção inválida!")
