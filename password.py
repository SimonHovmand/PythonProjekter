from pickle import TRUE

password = "2022"

login = False

falsecount = 0

while login == False:

    user_password = input("Hvad er dit password?\n")

    if user_password == password:
        print("Password correct!\n")
    else:
        print("Password incorrect!\n")   
        falsecount = falsecount + 1
 
