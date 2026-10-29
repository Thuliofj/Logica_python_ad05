while True:
  numero1 = float(input("Digite o primeiro numero: "))
  numero2 = float(input("Digite o segundo numero: "))
  operador = input(
      "Digite um operador (+, -, *, /) ou 'sair' para encerrar: "
  )

  # Se o usuário digitar sair, o loop é interrompido
  if operador.lower() == "sair":
    print("Encerrando a calculadora. Até mais!")
    break

  if operador == "+":
    soma = numero1 + numero2
    print(soma)

  elif operador == "-":
    subtracao = numero1 - numero2
    print(substracao)

  elif operador == "*":
    multiplicacao = numero1 * numero2
    print(multiplicacao)

  elif operador == "/":
    if numero2 == 0:
      print("Não é possível dividir por zero")
    else:
      divisao = numero1 / numero2
      print(divisao)
  else:
    print("Operador Inválido")

  print()