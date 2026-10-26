nomes_aprovados = ["Joao", "Maria", "Pedro", "Mariana"]

nome = input("Digite o seu nome: ").strip()

if nome.lower() in [n.lower() for n in nomes_aprovados]:
    print (f"{nome.capitalize()} você está aprovado!")
else:
    print(f"{nome.capitalize()} você está reprovado bobão")