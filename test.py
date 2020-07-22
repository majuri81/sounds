import random

# Implement Score System <<<

score = 0
lost = False
test = False

print("Aluksi sinulla ei ole pisteitä, mutta aina kun voitat tietokoneen, ansaitset yhden pisteen. Tasapelistä ei "
      "menetä kukaan pisteitä. Jos pisteesi "
      "tippuu alle nollan, niin häviät pelin.")

while not test:

    while lost:
        print("Hävisit pelin, koska pisteesi olivat alle 0.")
        ask = input("Uudestaan? ").lower().strip()
        if ask == "kyllä":
            score = 0
            lost = False
            test = False
            print("Peli aloitettu uudestaan.")
        elif ask == "ei":
            exit("Quitting..")
        elif ask.isdigit():
            print("Tuo on numero, eikä kivi, paperi tai sakset. Miten sää voit vahingossa kirjoittaa numeron, "
                  "ei jestas.")
            exit("Quitting..")
        else:
            print("Tuo ei ole yksi vaihtoehdoista (kyllä/ei)")
            exit("Quitting..")

    options = ["Kivi", "Paperi", "Sakset"]

    computer = options[random.randint(0, 2)]
    print("Pisteet: " + str(score))
    ask = input("Kivi, Paperi vai Sakset? ").lower().strip()

    if ask == "kivi":
        print("Valitsit kiven. Tietokone valitsi", computer)

        if computer == "Kivi":
            print("Tasapeli.")
            test = False

        if computer == "Paperi":
            print("Tietokone voitti.")
            score -= 1

            if score < 0:
                lost = True

        if computer == "Sakset":
            print("Sinä voitit.")
            score += 1

    elif ask == "paperi":
        print("Valitsit paperin. Tietokone valitsi", computer)

        if computer == "Paperi":
            print("Tasapeli.")
            test = False

        if computer == "Sakset":
            print("Tietokone voitti.")
            score -= 1

            if score < 0:
                lost = True

        if computer == "Kivi":
            print("Sinä voitit.")
            score += 1

    elif ask == "sakset":
        print("Valitsit sakset. Tietokone valitsi", computer)

        if computer == "Sakset":
            print("Tasapeli.")
            test = False

        if computer == "Kivi":
            print("Tietokone voitti.")
            score -= 1

            if score < 0:
                lost = True

        if computer == "Paperi":
            print("Sinä voitit.")
            score += 1
