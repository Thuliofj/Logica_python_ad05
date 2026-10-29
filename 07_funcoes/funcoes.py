#Funcao
def sobre():
    print("Desenvolvido por: ThulioFJ")
# Função sem retorno com parâmetros
def turma(turma, ano):
    print(f"Turma: {turma} - {ano}")

#Funcao com retorno e com parametros
def somar(batata1, batata2):
    return batata1 + batata2

sobre()
turma("AD-05", 2026)

numero1 = float(input("Digite o primeiro numero:"))
numero2 = float(input("Digite o segundo numero:"))

resultado = somar(numero1, numero2)

print(f"A soma é = {resultado}")