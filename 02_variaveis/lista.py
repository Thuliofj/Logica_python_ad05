#lista já pre definida
lista = [
    "Gabriel", 
    "Vinicius",
    "Jussara",
    "Priscilla",
    "Mauricio",
    "Josiane"
]
#mostrar a lista toda
print (lista)
#mostrar uma pessoa ou parte da lista especifica
print (lista[3])
#adiciona algo no final lista , so pode um item
lista.append("Felipe")

print (lista)
#insere em uma posicao especifica
lista.insert(0, "Rafael")

print (lista)
#remove o nome mesmo que tenha 2 nomes
lista.remove("Jussara")

print(lista)
# input para adicionar um nome no final
lista.append(input("Digite um nome:"))

print (lista)
#adiciona outra lista a lista
lista += ["Carlos", "Mariana", "Pedro"]
print(lista)
#pop remove um item especifico indicando indice
lista.pop(2)
 
print(lista)