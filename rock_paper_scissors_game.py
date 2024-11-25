import random

choices = ["rock", "paper", "scissors"]

# machine_choice = random.choice(choices)
def jatek():
    nyerések = 0
    vesztések = 0
    döntetlenek = 0

    # üdvözlő üzenet
    print("Üdvözöllek a Kő, Papír, Olló játékban!")

    while True:
        # felhasználó választása
        valasztas = input("Válassz karaktert: Kő, Papír, Olló -> ").lower()

        # érvénytelen választás
        while valasztas not in ['kő', 'papír', 'olló']:
            print("Érvénytelen válasz! Kérlek válassz a következők közül: kő, papír, olló.")
            valasztas = input("Válassz karaktert: Kő, Papír, Olló -> ").lower()

        # angol
        if valasztas == "kő":
            user_choice = "rock"
        elif valasztas == "papír":
            user_choice = "paper"
        else:
            user_choice = "scissors"

        # bot választása
        gep_valasztas = random.choice(choices)
        print(f"Gép válasza: {gep_valasztas}")

        # eredmény
        if user_choice == gep_valasztas:
            print("Döntetlen!")
            döntetlenek += 1
        elif (user_choice == 'rock' and gep_valasztas == 'scissors') or \
             (user_choice == 'paper' and gep_valasztas == 'rock') or \
             (user_choice == 'scissors' and gep_valasztas == 'paper'):
            print("Nyertél!")
            nyerések += 1
        else:
            print("Vesztettél!")
            vesztések += 1

        # eredmények kiírása
        print(f"nyerések: {nyerések}, vesztések: {vesztések}, döntetlenek: {döntetlenek}")

        # új játék
        uj_jatek = input("Akarsz még játszani? (i/n) ").lower()
        if uj_jatek != 'i':
            break

    # vége
    print(f"Köszönjük a játékot! A végső eredmény: {nyerések} győzelem, {vesztések} vereség, {döntetlenek} döntetlen.")

# játék indítása
jatek()
