def ehinteiro(numero):
  return numero == int(numero)


def ehpar(numero):
  if ehinteiro(numero):
    return int(numero) % 2 == 0
  return False


print("=== CALCULADORA INTELIGENTE ===\n")

resultado = float(input("Digite um numero: "))
historico = [resultado]

while True:
  operador = input(
      "Digite um operador (+, -, *, /), 'limpar' para recomeçar ou 'sair': "
  )

  if operador.lower() == "sair":
    print("\nEncerrando a calculadora. Até mais!")
    break

  if operador.lower() == "limpar":
    print("\n--- Calculadora Limpa ---\n")
    resultado = float(input("Digite um numero: "))
    historico = [resultado]
    continue

  if operador not in ("+", "-", "*", "/"):
    print("⚠️ Operador Inválido! Tente novamente.\n")
    continue

  numero = float(input("Digite um numero: "))

  if operador == "/" and numero == 0:
    print("⚠️ Erro: Não é possível dividir por zero!\n")
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
  print("Resultado:", *historico, "=", resultado)

  status_inteiro = "Sim" if ehinteiro(resultado) else "Não"
  status_par = "Sim" if ehpar(resultado) else "Não"

  print(f"  ↳ É inteiro? {status_inteiro} | É par? {status_par}")
  print()