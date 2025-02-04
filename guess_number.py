import random
from colorama import init, Fore as fr

init()
yellow = fr.YELLOW
green = fr.GREEN
default = fr.BLACK
red = fr.RED
white = fr.WHITE

n_choices = 0

print(f"{default}Seja muito bem vindo ao Guess Number do KG{yellow}")

random_number = random.randrange(1, 10)

while True:
    answer_user = int(input(f"{yellow}Adivinhe o número de 1 a 10: "))

    n_choices = n_choices + 1

    if answer_user == random_number:
        print(f"{green}Acertou!")
        break
    elif answer_user > random_number:
        print(f"{red}Chute alto, o número é menor que isso..")
    else:
        print(f"{red}Chute baixo, o número é maior que isso..")

print(f"{yellow}N° de tentativas: " + str(n_choices))