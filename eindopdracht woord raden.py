import random

def choose_word():
    word_list = ["scoutingkamp", "leon", "schoolkrant", "roodborstje", "Schaken", "kippen", "bbq","metis","aap", "dnd", "schaakmat", "printmachine", "tesla", "lieve", "explosie", "gevangenis", "achraf", "tekenen", "zwemmen", "tomtom", "computer", "hangman", "potkast", "gamer", "lamp", "schoen", "sterrenhemel",
 "judo", "anime", "ijsbeer","krukken","appelsap","lars","boom","winkelmandje","nokia","regenpijp","koe","vuurtoten","kaneel","stagere","muis","tas","Epibreren","ziel","nestel","Ferrule","monitor","schoolkrant","hoer","legoblokje","aansprakelijkheidswaardevaststellingsveranderingen","verzekeringskosten","muis","abrikosejam" ]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "-"
    return display

def hangman():
    max_attempts = 10
    word = choose_word()
    guessed_letters = []
    attempts = 0

    print("Welkom bij Hangman!")
    print("Het woord heeft {} letters.".format(len(word)))
    print("Woord:", display_word(word, guessed_letters))

    while True:
        guess = input("Raad een letter of het hele woord: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Je hebt die letter al geraden!")
                continue
            guessed_letters.append(guess)

            if guess not in word:
                attempts += 1
                print("Helaas, {} zit niet in het woord.".format(guess))
                print("Je hebt nog {} pogingen over.".format(max_attempts - attempts))
                if attempts >= max_attempts:
                    print("Je hebt te veel fouten gemaakt! Het woord was '{}'".format(word))
                    break
            else:
                print("Goed geraden!")

        elif len(guess) == len(word) and guess.isalpha():
            if guess == word:
                print("Gefeliciteerd! Je hebt het woord geraden: '{}'".format(word))
                break
            else:
                print("Helaas, dat is niet het juiste woord.")
                attempts += 1
                print("Je hebt nog {} pogingen over.".format(max_attempts - attempts))
                if attempts >= max_attempts:
                    print("Je hebt te veel fouten gemaakt! Het woord was '{}'".format(word))
                    break
        else:
            print("Ongeldige invoer. Voer slechts één letter in of het hele woord.")

        print("Woord:", display_word(word, guessed_letters))

        if all(letter in guessed_letters for letter in word):
            print("Gefeliciteerd! Je hebt het woord geraden: '{}'".format(word))
            break

    play_again = input("Wil je nog een keer spelen? (ja/nee): ")
    if play_again == "ja":
        hangman()
    else:
        print("Bedankt voor het spelen van Hangman!")

hangman()