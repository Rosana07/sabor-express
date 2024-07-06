print('\nPython na Escola de Programação da Alura\n')





# Criação das Variáveis
nome = 'Ro'
idade = 40

# Abordagem mais simples
print('Meu nome é',nome,'e tenho',idade,'anos.')

# Abordagem do f-string
print(f'Meu nome é {nome} e tenho {idade} anos.')

# Abordagem do .format()
print('Meu nome é {} e tenho {} anos.'.format(nome,idade))

# Abordagem da % (Formatação de String Antiga - Python 2)
print('Meu nome é %s e tenho %i anos.'%(nome,idade))

print('\nA','L','U','R','A',sep='\n')





pi = 3.14159

# Abordagem de f-string
print(f'\nO valor arredondado de pi é: {pi:.2f}')

# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}'.format(pi))

# Utilizando a função round()
print('O valor arredondado de pi é:', round(pi, 2))




#utilizando input() para coletar as informações e print() para exibir a mensagem formatada.
departamento = input("\nDigite o nome do departamento: ")
responsavel = input("Digite o nome da pessoa responsável: ")
print("O departamento de " + departamento + " é liderado por " + responsavel + ".\n")