#Crie um programa simples de Lista de Tarefas (TODOList) em Python que funcione no terminal.

lista_de_tarefas = []

while True:
    print("\n" + "="*30)
    print("      LISTA DE TAREFAS")
    print("="*30)
    print("1. Adicionar tarefa")
    print("2. Listar todas as tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")
    
    opcao = input("\nEscolha uma opção (1-5): ")
    
    if opcao == '1':
        nome_tarefa = input("Digite o nome da nova tarefa: ")
        nova_tarefa = {"nome": nome_tarefa, "feito": False}
        lista_de_tarefas.append(nova_tarefa)
        print(f"Tarefa '{nome_tarefa}' adicionada com sucesso!")
        
    elif opcao == '2':
        print("\n--- Suas Tarefas ---")
        if len(lista_de_tarefas) == 0:
            print("A lista está vazia.")
        else:
            for indice, tarefa in enumerate(lista_de_tarefas, 1):
                if tarefa["feito"] == True:
                    status = "FEITO"
                else:
                    status = "ESPERA"
                print(f"{indice}. {tarefa['nome']} - [{status}]")
                
    elif opcao == '3':
        if len(lista_de_tarefas) == 0:
            print("A lista está vazia. Não há tarefas para concluir.")
            continue
            
        entrada = input("Digite o número da tarefa para marcar como concluída: ")
        try:
            indice_tarefa = int(entrada) - 1
            if 0 <= indice_tarefa < len(lista_de_tarefas):
                lista_de_tarefas[indice_tarefa]["feito"] = True
                print("Tarefa marcada como concluída!")
            else:
                print("Erro: Número de tarefa não encontrado.")
        except ValueError:
            print("Erro: Por favor, digite apenas números válidos.")
            
    elif opcao == '4':
        if len(lista_de_tarefas) == 0:
            print("A lista está vazia. Não há tarefas para remover.")
            continue
            
        numero_tarefa = input("Digite o número da tarefa que deseja remover: ")
        try:
            indice_tarefa = int(numero_tarefa) - 1
            if 0 <= indice_tarefa < len(lista_de_tarefas):
                tarefa_removida = lista_de_tarefas.pop(indice_tarefa)
                print(f"Tarefa '{tarefa_removida['nome']}' removida com sucesso!")
            else:
                print("Erro: Número de tarefa não encontrado.")
        except ValueError:
            print("Erro: Por favor, digite apenas números válidos.")
            
    elif opcao == '5':
        print("Saindo do programa. Até logo!")
        break
        
    else:
        print("Opção inválida. Tente novamente.")