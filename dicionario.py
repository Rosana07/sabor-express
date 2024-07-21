pessoa = {'Nome':'Rosana', 'Idade':'42', 'Cidade': 'Belo Horizonte'}
print(pessoa)

#Atualização de valor (atualização da idade)
pessoa['Idade'] = 31
print(pessoa)


#Adicionar um item (adicionado profissão)
pessoa['Profissão'] = "ADS"
print(pessoa)


#Remover uma informação (remoção de elemento)
del pessoa['Idade']
print(pessoa)


#possivel abordagem para criar um dicionário que apresente os números de 1 a 5 e seus 
# respectivos quadrados:
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)


#Verificar a existencia de uma chave no dicionario
pessoa = { 'nome':'Amanda', 'idade': '19', 'cidade':'São Luiz'}
if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário." )

#contar a frequencia de cada palavra em uma frase
frase = "Python se tornou uma das linguagens de programação mais ppulares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1

print(contagem_palavras)