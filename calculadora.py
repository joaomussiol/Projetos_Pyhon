while True:
    num1 = float(input("Digite o primeiro numero: "))
    operador = input("Digite um operador. Ele pode ser. +, -, *, / : ")
    num2 = float(input("Digite o segundo numero: "))
    resultado = None

    if operador == "+" :
        resultado = num1 + num2

    elif operador == "-" :
        resultado = num1 - num2

    elif operador == "/" :
        if num2 == 0:
            print("ERRO, DIVISÃO POR ZERO")
        else:
            resultado = num1 / num2

    elif operador == "*" :
        resultado = num1 * num2

    else:
        print("Operador invalido")

    if resultado is not None:
        print(f"{num1} {operador} {num2} = {resultado}")

    continuar = input("Deseja continuar? (S/N): ").lower().strip()

    while continuar not in ["s", "n" ]:
        continuar = input("Digite apenas S ou N: ").lower().strip()

    if continuar == ("n"):
        break