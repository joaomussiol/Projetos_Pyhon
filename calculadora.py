num1 = float(input("Digite o primeiro numero: "))
operador = input("Digite um operador. Ele pode ser. +, -, *, / : ")
num2 = float(input("Digite o segundo numero: "))

if operador == "+" :
    resultado = num1 + num2
    print("Resultado é:",resultado)

elif operador == "-" :
    resultado = num1 - num2
    print("Resultado é:",resultado)

elif operador == "/" :
    try:
        resultado = num1 / num2
        print("Resultado é:",resultado)
    except Exception as e:
        print(e)

elif operador == "*" :
    resultado = num1 * num2
    print("Resultado é:", resultado)

else:
    print("operador invalido")