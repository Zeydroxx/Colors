import os

def afficher_dessin(numero, couleur):
    code_couleur = f"\033[{couleur}m"  # Code d'échappement ANSI pour la couleur
    reset_couleur = "\033[0m"  # Réinitialiser la couleur
    if numero == 1:
        print(f"{code_couleur}Dessin 1{reset_couleur}")
        print(f"{code_couleur}| $$  \\__/{reset_couleur}")
        print(f"{code_couleur}|  \\____  $${reset_couleur}")
        print(f"{code_couleur}| /$$  \\ $${reset_couleur}")
        print(f"{code_couleur}|  \\______/ {reset_couleur}")
    elif numero == 2:
        print(f"{code_couleur}Dessin 2{reset_couleur}")
        print(f"{code_couleur}  /$$$$$$ {reset_couleur}")
        print(f"{code_couleur} /$$__  $${reset_couleur}")
        print(f"{code_couleur}| $$  \\__/{reset_couleur}")
        print(f"{code_couleur}|  $$$$$$ {reset_couleur}")
        print(f"{code_couleur} \\____  $${reset_couleur}")
        print(f"{code_couleur} /$$  \\ $${reset_couleur}")
        print(f"{code_couleur}|  $$$$$$/{reset_couleur}")
        print(f"{code_couleur} \\______/ {reset_couleur}")
    elif numero == 3:
        print(f"{code_couleur}Dessin 3{reset_couleur}")
        print(f"{code_couleur}  _____  {reset_couleur}")
        print(f"{code_couleur} / ____|{reset_couleur}")
        print(f"{code_couleur}| |  __  {reset_couleur}")
        print(f"{code_couleur}| | |_ | {reset_couleur}")
        print(f"{code_couleur}| |__| |{reset_couleur}")
        print(f"{code_couleur} \\______|{reset_couleur}")
    elif numero == 4:
        print(f"{code_couleur}Dessin 4{reset_couleur}")
        print(f"{code_couleur}   /\\/\\   {reset_couleur}")
        print(f"{code_couleur}  /    \\  {reset_couleur}")
        print(f"{code_couleur} /      /\\{reset_couleur}")
        print(f"{code_couleur} \\ \\_/  / {reset_couleur}")
        print(f"{code_couleur}  \\   /  {reset_couleur}")
        print(f"{code_couleur}   \\/_/   {reset_couleur}")
    elif numero == 5:
        print(f"{code_couleur}Dessin 5{reset_couleur}")
        print(f"{code_couleur}   .----.   {reset_couleur}")
        print(f"{code_couleur}  /    \\  {reset_couleur}")
        print(f"{code_couleur} |  .-. ;  |{reset_couleur}")
        print(f"{code_couleur} |  | | |  |{reset_couleur}")
        print(f"{code_couleur}  \\  '-  /  {reset_couleur}")
        print(f"{code_couleur}   `----`   {reset_couleur}")
    elif numero == 6:
        print(f"{code_couleur}Dessin 6{reset_couleur}")
        print(f"{code_couleur}  _______  {reset_couleur}")
        print(f"{code_couleur} /  _____|{reset_couleur}")
        print(f"{code_couleur}|  |  __  {reset_couleur}")
        print(f"{code_couleur}|  | |_ | {reset_couleur}")
        print(f"{code_couleur}|  |__| |{reset_couleur}")
        print(f"{code_couleur} \\______|{reset_couleur}")
    elif numero == 7:
        print(f"{code_couleur}Dessin 7{reset_couleur}")
        print(f"{code_couleur}  ______  {reset_couleur}")
        print(f"{code_couleur} /  __  \\{reset_couleur}")
        print(f"{code_couleur}|  |  |  |{reset_couleur}")
        print(f"{code_couleur}|  |  |  |{reset_couleur}")
        print(f"{code_couleur}|  |__|  |{reset_couleur}")
        print(f"{code_couleur} \\______/ {reset_couleur}")
    elif numero == 8:
        print(f"{code_couleur}Dessin 8{reset_couleur}")
        print(f"{code_couleur}   _____  {reset_couleur}")
        print(f"{code_couleur}  /     \\{reset_couleur}")
        print(f"{code_couleur} /  /_\\  \\{reset_couleur}")
        print(f"{code_couleur}/  _____  \\{reset_couleur}")
        print(f"{code_couleur}\\_/     \\_/{reset_couleur}")
    elif numero == 9:
        print(f"{code_couleur}Dessin 9{reset_couleur}")
        print(f"{code_couleur}   ______  {reset_couleur}")
        print(f"{code_couleur}  /  __  \\{reset_couleur}")
        print(f"{code_couleur}|  |  |  |{reset_couleur}")
        print(f"{code_couleur}|  |  |  |{reset_couleur}")
        print(f"{code_couleur}|  |__|  |{reset_couleur}")
        print(f"{code_couleur} \\______/ {reset_couleur}")
    elif numero == 10:
        print(f"{code_couleur}Dessin 10{reset_couleur}")
        print(f"{code_couleur}   ______  {reset_couleur}")
        print(f"{code_couleur}  /  __  \\{reset_couleur}")
        print(f"{code_couleur}|  |  |  |{reset_couleur}")
        print(f"{code_couleur}|  |  |  |{reset_couleur}")
        print(f"{code_couleur}|  |__|  |{reset_couleur}")
        print(f"{code_couleur} \\______/ {reset_couleur}")
    else:
        print("Nombre hors de la plage de 1 à 10")

# Couleurs : 31 (rouge), 32 (vert), 33 (jaune), 34 (bleu), 35 (rose), 36 (cyan)
couleurs = ['31', '32', '33', '34', '35', '36']

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Effacer la console

    # Demander à l'utilisateur de saisir un nombre de 1 à 10
    numero = int(input("Entrez un nombre de 1 à 10 : "))

    # Sélectionner une couleur en fonction de l'itération
    couleur = couleurs[numero % len(couleurs)]

    # Afficher le dessin correspondant avec la couleur sélectionnée
    afficher_dessin(numero, couleur)

    recommencer = input("Appuyez sur Entrer pour recommancer : ")
    if recommencer.lower() != '':
        break
