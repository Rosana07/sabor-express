#Para criar as listas, podemos utilizar as seguintes variáveis:
lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
print(f'Lista de numeros: {lista_de_numeros}')

lista_de_nomes = ['emy','gui','lais','mari']
print(f'\nLista de nomes: {lista_de_nomes}')

lista_de_anos = [1981,2024]
print(f'\nLista de anos: {lista_de_anos}')




#percorrer todos os itens de uma lista com o loop for
lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in lista_de_numeros:
    print(numero)




#calcular a soma dos números impares de 1 a 10, 
#O segundo argumento de da função range é exclusivo, então range(1, 11) inclui números 
# de 1 a 10) com um passo de 2 (o terceiro argumento de range). Isso garante que apenas 
# números ímpares sejam considerados.
soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(f'\nA soma dos numeros ímpares informados é: {soma_impares}')



#imprimir os números de 1 a 10 de forma decrescente
for i in range(10, 0, -1):
    print(i)



#tabuada interativa
numero_tabuada = int(input("\nDigite um número para a tabuada: "))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")



#soma dos elementos de uma lista com for e usar try except para validar, 
#Exception é uma classe base para todas as exceções em Python. Capturar Exception permite 
# lidar com qualquer tipo de exceção que possa ocorrer no bloco try. O as e é opcional, mas 
# é frequentemente usado para acessar informações detalhadas sobre a exceção, como mensagens
#  de erro.
lista_numeros = [10, 5, 8, 3, 7]
soma = 0
print(f'\n{lista_numeros}')

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")


#Um modo de solucionar essa questão com uma validação de lista vazia é do seguinte modo:
#ZeroDivisionError é uma exceção específica que ocorre quando há uma tentativa de divisão 
# por zero. Este bloco except é destinado a lidar especificamente com esse tipo de erro.

lista_valores = [15, 20, 25, 30]
soma_valores = 0
print(f'\n{lista_valores}')

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")


