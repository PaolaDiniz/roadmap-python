import os

def visualizar(lista_compras):
    '''
    Mostra minha lista de compras.

    Inputs:
        lista_compras (list) --> lista com strings dos itens de compra.
    '''

    print('Itens da minha lista:\n')
    # intera sobre cada item da lista de compras
    for index, item in enumerate(lista_compras):
        print(f'Item {index}: {item};')
    print('\n')
    os.system('pause')

def add(lista_compras):
    '''
    Função que adiciona itens a nossa lista de compras.

    Inputs:
        lista_compras (list) --> lista com strings dos itens de compra.
    
    Returns:
        lista_compras (list) --> lista atualizada com strings dos itens de compra.
    '''

    print('Adicionando itens a lista de compras.\n')
    novo_item = str(input('Informe o item a ser adicionado a lista: '))

    return lista_compras.append(novo_item)

def remove(lista_compras):
    '''
    Função que remove itens da nossa lista de compras.

    Inputs:
        lista_compras (list) --> lista com strings dos itens de compra.
    
    Returns:
        lista_compras (list) --> lista atualizada com strings dos itens de compra.
    '''

    print('Removendo itens a lista de compras.\n')
    novo_item = str(input('Informe o item a ser removido da lista: '))

    try:
        lista_compras.remove(novo_item)
        os.system('cls')
        print('Item removido com sucesso!')
        os.system('pause')
    except:
        print('\nO item não está na lista de compras...')
        os.system('pause')
    
    return lista_compras


def main():
    '''
    Função Principal do Programa
    '''

    compras = list()
    escolha = 0

    # menu da aplicação de lista de compras
    while escolha != 4:
        print('=== Lista de Compras ===\n')
        print('1 - Adicionar itens.')
        print('2 - Remover itens.')
        print('3 - Visualizar a lista.')
        print('4 - Encerrar programa.')
        escolha = int(input('Escolha uma opção: '))

        # limpa o terminal de comandos
        os.system('cls')

        # chama a função que adiciona itens a lista de compras
        if escolha == 1:
            add(compras)
            os.system('cls')
        # chama a função que remove itens da lista de compras
        if escolha == 2:
            remove(compras)
            os.system('cls')
        # chama a função que imprime a lista de compras na tela
        if escolha == 3:
            visualizar(compras)
            os.system('cls')
        # verifica a entrada do usuário
        if escolha < 1 or escolha > 4:
            print('Entrada inválida. Tente novamente...\n')
            os.system('pause')
            os.system('cls')


if __name__ == '__main__':
    main()