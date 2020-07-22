import random
import time

rand1 = random.randint(1, 6)  # 6
rand2 = random.randint(1, 12)  # 12
rand3 = random.randint(1, 24)  # 24
rand4 = random.randint(1, 48)  # 48
rand5 = random.randint(1, 96)  # 96

score = 0
totalguesses = 0
guessesleft = 3
print("Sinulla on kolme arvausta käytettävissä tasoilla 1 ja 2.")
print("Taso 1.")

start = time.time()

while guessesleft > 0:

    ask = int(input("Arvaa numero väliltä 1 ja 6: "))

    if ask != rand1:
        guessesleft -= 1
        totalguesses += 1
        print('\n' + "Väärin! Sinulla on", guessesleft, "yritystä jäljellä.")

    if guessesleft > 0 and ask < rand1:
        totalguesses += 1
        print("Numero on isompi!")

    if guessesleft > 0 and ask > rand1:
        totalguesses += 1
        print("Numero on pienempi!")

    if ask == rand1:
        print("Oikein!")
        print("Taso 2.")
        guessesleft = 3
        taso2 = True

        while taso2 and guessesleft > 0:
            ask2 = int(input("Arvaa numero väliltä 1 ja 12: "))

            if ask2 != rand2:
                guessesleft -= 1
                totalguesses += 1
                print('\n' + "Väärin! Sinulla on", guessesleft, "yritystä jäljellä.")

            if guessesleft > 0 and ask2 < rand2:
                totalguesses += 1
                print("Numero on isompi!")

            if guessesleft > 0 and ask2 > rand2:
                totalguesses += 1
                print("Numero on pienempi!")

            if ask2 == rand2:
                print("Oikein! Läpäisit tason.")
                guessesleft = 5
                print("Taso 3.")
                print("Sinulla on nyt enemmän arvauksia, koska taso on vaikeampi. Arvauksia on yhteensä 5.")
                taso3 = True

                while taso3 and guessesleft > 0:
                    ask3 = int(input("Arvaa numero väliltä 1 ja 24: "))

                    if ask3 != rand3:
                        guessesleft -= 1
                        totalguesses += 1
                        print("Väärin! Sinulla on", guessesleft, "yritystä jäljellä.")

                    if guessesleft > 0 and ask3 < rand3:
                        totalguesses += 1
                        print("Numero on isompi!")

                    if guessesleft > 0 and ask3 > rand3:
                        totalguesses += 1
                        print("Numero on pienempi!")

                    if ask3 == rand3:
                        print("Oikein! Läpäisit tason.")
                        guessesleft = 5
                        print("Taso 4.")
                        print("Arvauksia on yhteensä 5.")
                        taso4 = True

                        while taso4 and guessesleft > 0:
                            ask4 = int(input("Arvaa numero väliltä 1 ja 48: "))

                            if ask4 != rand4:
                                totalguesses += 1
                                guessesleft -= 1
                                print("Väärin! Sinulla on", guessesleft, "yritystä jäljellä.")

                            if guessesleft > 0 and ask4 < rand4:
                                totalguesses += 1
                                print("Numero on isompi!")

                            if guessesleft > 0 and ask4 > rand4:
                                totalguesses += 1
                                print("Numero on pienempi!")

                            if ask4 == rand4:
                                print("Oikein! Läpäisit tason.")
                                guessesleft = 10
                                print("Taso 5.")
                                print(
                                    "Sinulla on nyt enemmän arvauksia, koska taso on vaikeampi. "
                                    "Arvauksia on nyt yhteensä 10.")
                                taso5 = True

                                while taso5 and guessesleft > 0:
                                    ask5 = int(input("Arvaa numero väliltä 1 ja 96: "))

                                    if ask5 != rand5:
                                        totalguesses += 1
                                        guessesleft -= 1
                                        print("Väärin! Sinulla on", guessesleft, "yritystä jäljellä.")

                                    if guessesleft > 0 and ask5 < rand5:
                                        totalguesses += 1
                                        print("Numero on isompi!")

                                    if guessesleft > 0 and ask5 > rand5:
                                        totalguesses += 1
                                        print("Numero on pienempi!")

                                    if ask5 == rand5:
                                        print("Oikein! Voitit pelin!")
                                        print("Tilastot:")
                                        print("Jouduit arvaamaan yhteensä", totalguesses, "kertaa pelin aikana.")

                                        # ihme scripti

                                        end = time.time()
                                        temp = end - start
                                        minutes = temp // 60
                                        seconds = temp - 60 * minutes
                                        print("Aikaa sinulla meni:", '%d.%d' % (minutes, seconds) + "s")

                                        if totalguesses < 15:
                                            print("Arvio: Erinomainen! ;) ")

                                        if 10 <= totalguesses <= 20:
                                            print("Arvio: Hyvä! :) ")

                                        if 15 < totalguesses <= 25:
                                            print("Arvio: Kohtalainen. :| ")

                                        if 20 < totalguesses <= 30:
                                            print("Arvio: Huono. :/ ")

                                        if totalguesses > 35:
                                            print("Arvio: Todella huono. :( ")

                                        exit()

                                else:
                                    totalguesses += 1
                                    print("Sinun arvaukset loppuivat kesken. Numero olisi ollut", rand5)
                                    exit("Hävisit pelin.")
                        else:
                            totalguesses += 1
                            print("Sinun arvaukset loppuivat kesken. Numero olisi ollut", rand4)
                            exit("Hävisit pelin.")
                else:
                    totalguesses += 1
                    print("Sinun arvaukset loppuivat kesken. Numero olisi ollut", rand3)
                    exit("Hävisit pelin.")
        else:
            totalguesses += 1
            print("Sinun arvaukset loppuivat kesken. Numero olisi ollut", rand2)
            exit("Hävisit pelin.")

totalguesses += 1
print("Sinun arvaukset loppuivat kesken. Numero olisi ollut", rand1)
exit("Hävisit pelin.")
