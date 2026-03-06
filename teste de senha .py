print("agora faremos o seu cadastro")
username = input("diga seu nome de usuario: ")
user_password = int(input("digite sua senha de usuario: "))
max_trys = 3

print("agora iremos fazer login")

for tentativas in range(1, max_trys +1 ):
    username_digitado = input
    senha_digitada = int(input("digite sua senha:"))

    if senha_digitada == user_password:
        print("acertou")
        break
    else:
        print("errou")