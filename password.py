
password = "2022"

login = 0

falsecount = 0

while login == 0:

    user_password = input("Hvad er dit password?\n")

    if user_password == password:
        print("Password correct!\n")
        login += 1
        break

    elif falsecount >= 2:
        password_reset = input("Ønsker du at nulstille dit password? Y/N: ")

        if password_reset == "Y" or "y":
            falsecount = 0
            New_password = input("\nHvad skal dit nye password være?\n")
            if New_password == password:
                print("Du kan ikke bruge det samme password!")
            else:
                password = New_password
        else:
            print("I orden")
            falsecount = 0
    elif user_password == "Debug":
        print("\n!!!Debug!!!")
        print(password)
        print(falsecount)
        print("!!!Debug!!!\n")

    else:
        print("Password incorrect!\n")   
        falsecount += 1