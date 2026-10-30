def ehinteiro(numero):
  return numero == int(numero)

def ehpar(numero):
  if ehinteiro(numero):
    return int(numero) % 2 == 0
  return False

resultado = float(input("Digite um numero: "))
historico = [resultado]

while True:
  operador = input(
      "Digite um operador (+, -, *, /), 'limpar' para recomeçar ou 'sair': "
  )

  if operador.lower() == "sair":
    print("Encerrando a calculadora. Até mais!")
    break

  if operador.lower() == "limpar":
    resultado = float(input("Digite um numero: "))
    historico = [resultado]
    continue

  if operador not in ("+", "-", "*", "/"):
    print("Operador Inválido")
    continue

  numero = float(input("Digite um numero: "))

  if operador == "/" and numero == 0:
    print("Não é possível dividir por zero")
    continue

  if operador == "+":
    resultado = resultado + numero
  elif operador == "-":
    resultado = resultado - numero
  elif operador == "*":
    resultado = resultado * numero
  elif operador == "/":
    resultado = resultado / numero

  historico.append(operador)
  historico.append(numero)

  print(*historico, "=", resultado)

  print(
      f"-> O resultado atual ({resultado}) é inteiro? {ehinteiro(resultado)}"
  )
  print(f"-> O resultado atual ({resultado}) é par? {ehpar(resultado)}")
  print()