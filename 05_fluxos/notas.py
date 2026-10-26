nome = input("Digite a nome do aluno: ")
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))

while True:
    nota1 = float(input("Digite a primeira nota do aluno: "))
    if 0 <= nota1 <= 10:
        break  
    print("Nota inválida! A nota deve estar entre 0 e 10.")

while True:
    nota2 = float(input("Digite a segunda nota do aluno: "))
    if 0 <= nota2 <= 10:
        break  
    print("Nota inválida! A nota deve estar entre 0 e 10.")

media = (nota1 + nota2) / 2

if media >=7:
    print(f"{nome} foi aprovado(a) com a média {media}")
elif media  >= 5:
    print(f"{nome} está de exame com a média {media}")
else:
    print(f"{nome} foi reprovado(a) com a média {media}")
