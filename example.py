from random import randint 

def password_checker(question, secret_word):
    while True:
        guess = input(question)
        if guess.isalpha() == False:
            print("Sorry, that is not an acceptable guess. Try again")
        elif len(guess) != len(secret_word):
            print(f"Sorry, that guess must be {len(secret_word)} letters long.")
        else:
            break
    return guess.lower()

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
descriptor_name = f"{descriptor.capitalize()} {name.upper()}"

secret_word = "aorta"

print(f"Ok {descriptor_name}, please guess what is the 5 letter password. \nYou'll have 5 tries")
intro_sentence = f"{descriptor_name}, please enter your first guess: \n"
subsequent_sentence = f"{descriptor_name}, please enter another guess: \n"

hints = [
    "Hint: it's in the body\n",
    "Hint: it carries oxygenated blood\n",
    "Hint: it's a major blood vessel\n",
    "Hint: its connected to the heart\n",
    "Oh no, you're out of tries! \nBetter luck next time! :("
]

for attempt in range(0,5):
    if attempt == 0:
        guess = password_checker(intro_sentence, secret_word)
    else:
        guess = password_checker(subsequent_sentence, secret_word)

    if guess == secret_word:
        print("You've got it!")
        break
    else:
        print("Sorry that's wrong!")
        print(hints[attempt])