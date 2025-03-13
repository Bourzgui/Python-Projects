import random

def number_guessing_game():
    print("Bienvenue dans le jeu de devinette !")
    print("Essayez de deviner le nombre entre 1 et 100.")
     
    random_number = random.randint(1, 100)

    max_attempts = 7

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Tentative {attempt}/{max_attempts} : Entrez votre nombre : "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        if guess < random_number:
            print("Trop bas ! Essayez encore.")
        elif guess > random_number:
            print("Trop haut ! Essayez encore.")
        else:
            print(f"Félicitations ! Vous avez trouvé le nombre {random_number} en {attempt} essais.")
            return   

    print(f"Dommage ! Le bon nombre était {random_number}. Mieux vaut essayer la prochaine fois.")

if __name__ == "__main__":
    number_guessing_game()
