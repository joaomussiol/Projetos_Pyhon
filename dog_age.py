print("welcome to the human dog age calculator")

dog_name = input("What is your dog name?: ")
dog_age = float(input("What is your dog age?: "))

new_dog_age = dog_age * 7

if dog_age >= 20:
    print("your dog isn't that old, he must have already died. i'm sorry")
else:
    print("the", dog_name, "has in human age:", new_dog_age, "years old")

