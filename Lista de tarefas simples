# Lista de Tarefas Simples

tarefas = []

def adicionar_tarefa():
    tarefa = input("Qual tarefa deseja adicionar?: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!\n")

def ver_tarefas():
    if not tarefas:
        print("Nenhuma tarefa na lista.\n")
    else:
        print("Lista de Tarefas:")
        for i, tarefa in enumerate(tarefas):
            print(f"{i + 1}. {tarefa}")
        print()

def remover_tarefa():
    ver_tarefas()
    if tarefas:
        try:
            indice = int(input("Digite o número da tarefa a ser removida da sua lista: ")) - 1
            if 0 <= indice < len(tarefas):
                tarefa_removida = tarefas.pop(indice)
                print(f"Tarefa '{tarefa_removida}' removida com sucesso!\n")
            else:
                print("Índice inválido.\n")
        except ValueError:
            print("Este não é um número válido.\n")

def menu():
    while True:
        print("Bem vindo(a) a lista de tarefas! Escolha uma das opçoês abaixo.")
        print("1. Adicionar uma tarefa")
        print("2. Ver tarefas adicionadas")
        print("3. Remover tarefa")
        print("4. Sair")
        opcao = input("Digite a opção escolhida: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            ver_tarefas()
        elif opcao == "3":
            remover_tarefa()
        elif opcao == "4":
            print("Até a próxima tarefa!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

menu()



