from random import randint 
while True:
    name  = input("Please enter your name: \n")
    try:
        float(name)
    except ValueError:
        break

number = randint(0,20)
print(f"Hello {name.upper()}!!! " * number)