# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 23:14:18 2021

@author: david
"""

#PYTHON -- PYTHON -- PYTHON
#Nesse post, iremos falar sobre LISTAS. Em qualquer linguagem de programação,
#Listas são muito úteis quando precisamos estruturar um grupo de dados,
#em uma estrutura linear, que podem ter tipos iguais e no caso da
#linguagem Python, as listas são interpretadas como objetos, assumindo 
#variados tipos, como STRING, NUMÉRICOS e até mesmo outras listas
#em sua composição. O consumo ou enfâse do tipo de cada elemento,
#somente é detalhado quando há uma necessidade ou processamento,
#que pode aplicar alguma iteração item a item.
#Uma lista possui em sua estruturação um índice que ajuda no acesso 
#ao valor da posição, iniciando com 0 até N valores definidos.

#Uma lista é representada por um ARRAY = [], que tem em sua composição
#valores separados por vírgulas. 

#Algumas listas possíveis
listaVazia = []

listaNumerica = [1,7,9,11]

listaTextual = ['python','java','c++','javascript']

listaDecimal = [10.2,11.7,12.9,15.8]

listaTudo = [12.9,'Python',1000,[1,2]]

#Printando os valores atribuídos de cada lista
print("Lista Vazia:")
print(listaVazia)
print("Lista Numérica:")
print(listaNumerica)
print("Lista Textual:")
print(listaTextual)
print("Lista Decimal:")
print(listaDecimal)
print("Lista Tudo:")
print(listaTudo)

#Para entendimento da estrutura, vamos aplicar algumas lógicas que 
#em desenvolvimento são muito úteis e necessárias para evolução e 
#tratamento de dados...

#Validando tamanho de uma lista
print("Mostrando o tamanho de uma lista:")
print(len(listaNumerica))

#Concatenando duas listas (JUNTANDO, rsrsrs)
print("Mostrando a união de duas listas:")
print(listaNumerica + listaTextual)

#Multiplicando listas 
print("Multiplicando uma lista:")
print(listaNumerica * 4)

#Iterando em uma lista 
for item in listaTextual:
    print("Valor: " + item)
    
#Validando se existe um valor específico em uma lista 
for item in listaTextual:
    if "python" == item: 
        print("Sim, Encontrei: " + item)
        

#A estrutura lista também possui algumas funções que ajudam na sua 
#organização, manutenção e manipulação, são elas,
#APPEND, INSERT, POP, REMOVE, COUNT, SORT e REVERSE        


#APPEND insere um novo registro para um índice subsequente na ordenação
print("Append novo registro")
listaTextual.append("NodeJs")
print(listaTextual)

#INSERT insere um novo registro para um índice definido 
print("Insert novo registro")
listaTextual.insert(0, "C#")
print(listaTextual)

#POP remove o último registro da lista ou o índice passado
print("Pop último registro")
listaTextual.pop()
print(listaTextual)
print("Pop primeiro registro pelo índice 0")
listaTextual.pop(0)
print(listaTextual)

#REMOVE remove um registro onde o índice é desconhecido
print("Remove um registro onde o índice é desconhecido")
listaTextual.remove("java")
print(listaTextual)

#COUNT conta a quantidade de itens que foram encotrados na lista
print("Contagem da quantidade de Itens iguais encontrados na lista")
print(listaTextual.count("c++"))

#SORT Ordena a lista em ordem crescente ou alfabética
print("Ordena a lista em ordem crescente ou alfabética")
listaTextual.sort()
print(listaTextual)

#REVERSE Reverte a posição dos elementos na lista
print("Reverte a posição dos elementos na lista")
listaTextual.reverse()
print(listaTextual)