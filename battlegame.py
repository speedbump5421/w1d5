Wizard = 1
Elf = 2
Human = 3
print("")
print("1)  Wizard")
print("2)  Elf")
print("3)  Human")

valid_options = {'1', '2', '3'}
while True:
    char = input("Choose your character: ")
    if char in valid_options:
        print("You selected " + char)
        break
    else:
        print("Unknown character")
        print("1)  Wizard")
        print("2)  Elf")
        print("3)  Human")


"""char = int(input("Choose your character: "))
while char >= 4:
    print("Unknown character")
    print("1)  Wizard")
    print("2)  Elf")
    print("3)  Human")
    pass"""
