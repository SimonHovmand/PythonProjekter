import random

count = 0


tall = int(input("Hvad skal det højeste tal være? (0 - X) "))

if tall >= 5:
    number = random.randint(0,tall)
else:
    print("Du skal have mere end 5 tal!")
    quit()

guesses = int(input("\nHvor mange gæt må man bruge? "))

if guesses >= tall:
    print("Du må ikke have flere gæt end det højeste tal!")
    quit()

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
    elif guess < number:
        print("Dit gæt er lavere end svaret!\n")
    elif guess > number:
        print("Dit gæt er højere end svaret!\n")

if count == guesses:
    print("\nNummeret var %d" % number)
    print("Bedre held næste gang!\n")