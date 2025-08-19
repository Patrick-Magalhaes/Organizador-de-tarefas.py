lista = []

print('='*50)
print('SEJA BEM-VINDO(A) AO ORGANIZADOR DE TAREFAS!!!')
print('='*50)
nome = input('Para começarmos, digite seu nome: ')
print(f'\nOlá, {nome}! Vamos começar?')

while True:
    print('\n' + '='*30)
    print('MENU DE ESCOLHA')
    print('[1] - Adicionar Tarefa')
    print('[2] - Listar Tarefas')
    print('[3] - Alterar Tarefa')
    print('[4] - Remover Tarefa')
    print('[5] - Sair')
    print('='*30)

    try:
        escolha = int(input('Insira sua escolha: '))
    except ValueError:
        print('Por favor, insira um número válido!')
        continue

    if escolha == 1:
        tarefa = input('Insira sua tarefa: ')
        lista.append(tarefa)
        print('Tarefa adicionada com sucesso!')

    elif escolha == 2:
        if lista:
            print('Tarefas:')
            for i, tarefa in enumerate(lista, 1):
                print(f'{i} - {tarefa}')
        else:
            print('Nenhuma tarefa cadastrada.')

    elif escolha == 3:
        if lista:
            print('Tarefas:')
            for i, tarefa in enumerate(lista, 1):
                print(f'{i} - {tarefa}')
            tarefa_antiga = input('Qual tarefa deseja alterar? ')
            if tarefa_antiga in lista:
                tarefa_nova = input('Insira a nova tarefa: ')
                indice = lista.index(tarefa_antiga)
                lista[indice] = tarefa_nova
                print('Tarefa alterada com sucesso!')
            else:
                print('Tarefa não encontrada!')
        else:
            print('Nenhuma tarefa para alterar.')

    elif escolha == 4:
        if lista:
            print('Tarefas:')
            for i, tarefa in enumerate(lista, 1):
                print(f'{i} - {tarefa}')
            remover = input('Qual tarefa deseja remover? ')
            if remover in lista:
                lista.remove(remover)
                print(f'Tarefa "{remover}" removida com sucesso!')
            else:
                print('Tarefa não encontrada!')
        else:
            print('Nenhuma tarefa para remover.')

    elif escolha == 5:
        print('Obrigado por utilizar nosso programa!')
        break
    else:
        print('Opção inválida. Tente novamente.')
