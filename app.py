import os

restaurantes = [{'nome':'Kony', 'categoria':'japonesa', 'ativo':'False'},
                {'nome':'Coco Banbu', 'categoria':"happyhour", 'ativo':'True'},
                {'nome':'Canela', 'categoria':'mexicana', 'ativo':'False'},]

def exibir_nome_do_programa():
    '''Exibe o nome estilizado do programa na tela'''

    print("""
      
        
░█▀▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ 　 ░█▀▀▀ █─█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ 
─▀▀▀▄▄ █▄▄█ █▀▀▄ █──█ █▄▄▀ 　 ░█▀▀▀ ▄▀▄ █──█ █▄▄▀ █▀▀ ▀▀█ ▀▀█ 
░█▄▄▄█ ▀──▀ ▀▀▀─ ▀▀▀▀ ▀─▀▀ 　 ░█▄▄▄ ▀─▀ █▀▀▀ ▀─▀▀ ▀▀▀ ▀▀▀ ▀▀▀
      
      """)


def exibir_opcoes():
    '''Exibe as opções disponiveis no menu principal'''
    print('1. Cadastrar Restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')


def voltar_ao_menu_principal():
    '''Solicita uma tecla para voltar ao menu principal
    
    Outputs:
    - Retorna ao menu princial
    '''
    input('\nDigite uma tecla para voltar ao menu ')
    main()
 

def opcao_invalida():
    '''Exibe mensagem de opção inválida e retorna ao menu principal
    
    Outputs:
    - Retorna ao menu principal
    '''
    print('Opção invalida!\n')
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    '''Exibe um subtitulo estilizado na tela
     
      Inputs
       - Texto: str - o texto do subtitulo
     '''
    os.system('cls')
    texto = texto.strip()
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante

Inputs:
- Nome do restaurante
- Categoria

Output:
- Adiciona um novo restaurante à lista de restaurantes
'''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {f'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    ''' Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''
    exibir_subtitulo('Listando os restaurantes')

    print(f'{'Nome do restaurante'.ljust(21)} | {'categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado' #Ternário
        print(f'-{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()



def alternar_estado_restaurante():
    ''' Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for i, restaurante in enumerate(restaurantes):
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            # Alternar o estado do restaurante
            restaurantes[i]['ativo'] = not restaurantes[i]['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurantes[i]['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            break  # Interrompe o loop após encontrar o restaurante
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')

    voltar_ao_menu_principal()




def escolher_opcao():
    ''' Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    opcao_escolhida = int(input('\nEscolha uma opção: '))
    # opcao_escolhida = int(opcao_escolhida)
    try:

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def finalizar_app():
    '''Exibe mensagem de finalização do aplicativo'''
    exibir_subtitulo('Finalizando o app')


def main():
    ''' Função principal que inicia o programa '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()