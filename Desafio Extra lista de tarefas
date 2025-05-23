#Desafio Extra

import os

tarefas = []

ARQUIVO_TAREFAS = "tarefas.txt"

def carregar_tarefas():
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                nome, status = linha.strip().split("||")
                tarefas.append({"nome": nome, "concluida": status == "1"})

def salvar_tarefas():
    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as arquivo:
        for tarefa in tarefas:
            status = "1" if tarefa["concluida"] else "0"
            arquivo.write(f"{tarefa['nome']}||{status}\n")

def adicionar_tarefa():
    nome = input("Digite a nova tarefa: ")
    tarefas.append({"nome": nome, "concluida": False})
    print("Tarefa adicionada com sucesso!\n")

def ver_tarefas():
    if not tarefas:
        print("Nenhuma tarefa na lista.\n")
    else:
        print("Lista de Tarefas:")
        for i, tarefa in enumerate(tarefas):
            status = "✔️" if tarefa["concluida"] else "❌"
            print(f"{i + 1}. {tarefa['nome']} [{status}]")
        print()

def remover_tarefa():
    ver_tarefas()
    if tarefas:
        try:
            indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
            if 0 <= indice < len(tarefas):
                removida = tarefas.pop(indice)
                print(f"Tarefa '{removida['nome']}' removida com sucesso!\n")
            else:
                print("Índice inválido.\n")
        except ValueError:
            print("Por favor, digite um número válido.\n")

def concluir_tarefa():
    ver_tarefas()
    if tarefas:
        try:
            indice = int(input("Digite o número da tarefa a marcar como concluída: ")) - 1
            if 0 <= indice < len(tarefas):
                tarefas[indice]["concluida"] = True
                print("Tarefa marcada como concluída!\n")
            else:
                print("Índice inválido.\n")
        except ValueError:
            print("Esse não é um número válido.\n")

def menu():
    carregar_tarefas()
    while True:
        print("Bem vindo(a) a lista de tarefas! Escolha uma das opçoês abaixo.")
        print("1. Adicionar tarefa")
        print("2. Ver tarefas")
        print("3. Remover tarefa")
        print("4. Marcar tarefa como concluída")
        print("5. Sair")
        opcao = input("Digite a opção escolhida: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            ver_tarefas()
        elif opcao == "3":
            remover_tarefa()
        elif opcao == "4":
            concluir_tarefa()
        elif opcao == "5":
            salvar_tarefas()
            print("Tarefas salvas com sucesso!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

menu()
