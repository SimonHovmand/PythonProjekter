import random
import string

stop = False

while stop == False:

    count = 0

    help = False

    tall = int(input("Hvad skal det højeste tal være? (0 - X)"))

    if tall >= 5:
        number = random.randint(0,tall)
    else:
        print("Du skal have mere end 5 tal!")
        quit()

    guesses = int(input("\nHvor mange gæt må man bruge? "))
    if guesses >= tall:
        print("Du må ikke have flere gæt end det højeste tal!")
        quit()

    help = (input("\nVil du hjælpes? Y/N "))

    if help == "Y" or help == "y":
        help = True
    else:
        help = False

    print("\nDu skal gætte et tal imellem 0 og", tall )
    print("Du har", guesses, "forsøg på at gætte det rigtige tal!")
    print("Held og lykke!\n")

    while count < guesses:
        guess = int(input("Dit gæt? "))
        count += 1
        if guess == number:
            print("\nDU GÆTTEDE RIGTIGT!")
            print("Du gættede det på", count, "gæt!\n")
            break
        elif help == True:
            if guess < number:
                print("Dit gæt er lavere end svaret!\n")
            if guess > number:
                print("Dit gæt er højere end svaret!\n")
        elif help == False:
            print("Forkert gæt, prøv igen\n")

    if count == guesses:
        print("\nNummeret var %d" % number)
        print("Bedre held næste gang!\n")

    tryagain = (input("Vil du prøve igen? Y/N\n"))

    if tryagain == "N" or tryagain == "n":
        stop = True
    else:
        stop = False