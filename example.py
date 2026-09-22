from random import randint 

def password_checker(question, secret_word):
    while True:
        password = input(question)
        if password.isalpha() == False:
            print("Sorry, that is not an acceptable guess. Try again")
        elif len(password) != len(secret_word):
            print(f"Sorry, that guess must be {len(secret_word)} letters long.")
        else:
            break
    return password

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

secret_word = "aorta"

print(f"Ok {descriptor_name}, please guess what is the 5 letter password. \nYou'll have 5 tries")
intro_sentence = f"{descriptor_name.capitalize()}, please enter your first guess"
subsequent_sentence = f"{descriptor_name.capitalize()}, please enter another guess: \n"

hints = [
    "Hint: it's in the body",
    "Hint: it carries oxygenated blood",
    "Hint: it's a major blood vessel",
    "Hint: its connected to the heart"
    "Sorry, you're out of tries! :("
]

