from random import randint 
while True:
    name  = input("Please enter your name: \n")
    if name.isalpha() == False:
        print("No name contains those characters!")
    else:
        break

while True:
    age = input("What's your age? \n")
    try:
        age = int(age)
        break
    except ValueError:
        print("You must enter your age as a numerical integer.")

number = randint(0,10)

if age <= 25:
    declaritive = "you're young and cool"
    number = round( (age + number) / 2)
    descriptor = "cool"
else:
    declaritive = "you're old and yucky"
    descriptor = "yucky"
    
print(f"Hello {name.upper()}, {declaritive}!!! " * number)
descriptor_name = f"{descriptor} {name.capitalize()}"

secret_word = "testy"