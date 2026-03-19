print("=== cadastro ===")
username = input("Digite seu nome de usuário: ")
user_password = (input("digite sua senha de usuario:"))

max_trys = 3

print("\n=== Login ===")

for tentativas in range(1, max_trys +1 ):
    username_digitado = input("Digite seu usuário: ")
    senha_digitada = (input("Digite sua senha:"))

    if username_digitado == username and senha_digitada == user_password:
        print("Login realizado com sucesso")
        break

    else:
        print(f"Erro! Tentativa {tentativas} de {max_trys}")

else:
    print("Limite de tentativas excedidas, Acesso Negado")