print("Vamos calcular a idade do seu cachorro em idade humana")
dog_name = input("Então me diga o nome do seu doguinho aí: ")
old_dog_age = float(input("e quantos anos o seu doguinho tem? "))
new_dog_age = float(old_dog_age * 7)
if new_dog_age >= 20:
    print("seu doguinho não é tão velho assim, diga a idade verdadeira dele aí")
else:
    print("Então o seu doguinho ",dog_name + "tem ",new_dog_age,"anos em idade humana.")
