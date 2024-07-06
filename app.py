import os


def exibir_nome_do_programa():

    print("""
      
      ssǝɹdxǝ ɹoqɐS
      
      """)


def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')


 

def escolher_opcao():
    opcao_escolhida = int(input('\nEscolha uma opção: '))
    # opcao_escolhida = int(opcao_escolhida)


    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar restaurantes')
    else:
        finalizar_app()


def finalizar_app():
    os.system('cls')
    # s.system('clear') no mac
    print('Finalizando o app\n')   


def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()