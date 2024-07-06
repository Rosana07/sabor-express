#verificar se um número é impar ou par, você pode fazer essa estrutura condicional:
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

#Para fazer as condicionais que informará a idade em categorias, 
# você pode usar essa estrutura:
idade = int(input("\nDigite sua idade: "))
if 0 < idade <= 12:
    print("Criança\n")
elif 12 < idade < 18:
    print("Adolescente\n")
elif idade >= 18:
    print("Adulto\n")
else: 
    print("Valor inválido!")


#Para fazer uma condicional que poderá verificar os valores de usuário e senha, 
# você pode utilizar o seguinte código:
usuario_correto = "alura"
senha_correta = "alura123"

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("\nLogin bem sucedido!\n")
else:
    print("\nCredenciais inválidas. Tente novamente.\n")

#Para verificar onde o ponto está localizado no plano cartesiano, 
# você pode utilizar a seguinte estrutura:
x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if x > 0 and y > 0:
    print("\nO ponto está no primeiro quadrante.\n")
elif x < 0 and y > 0:
    print("\nO ponto está no segundo quadrante.\n")
elif x < 0 and y < 0:
    print("\nO ponto está no terceiro quadrante.\n")
elif x > 0 and y < 0:
    print("\nO ponto está no quarto quadrante.\n")
else:
    print("O ponto está sobre um eixo ou na origem.")



