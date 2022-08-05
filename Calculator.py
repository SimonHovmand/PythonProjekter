import math

def calculate(num1, num2, act):
    if(act=="+"):
        total=num1+num2
    elif(act=="-"):
        total=num1-num2
    elif(act=="*"):
        total=num1*num2
    elif(act=="/"):
        total=num1/num2
    else:
        print("input not recognized")
    return total

def calc2():
    user_input=input("Enter a num1 act num2: ")
    var1, action, var2=user_input.split()
    if (action=="/" and var2=="0"):
        print("You cant devide by 0!")
    else:
        print(calculate(float(var1), float(var2), action))

def calc3():
    user_input=input("Enter num1 act1 num2 act2 num3: ")
    var1, action1, var2, action2, var3=user_input.split()
    if(action1=="/" and var2=="0" or action2=="/" and var3=="0"):
        print("You cant devide by 0!")
    elif((action2=="*" or action2=="/") and (action1=="+" or action2=="-")):
        total=calculate(float(var2), float(var3), action2)
        print(calculate(float(var1), float(total), action1))
    else:
        total=calculate(float(var1), float(var2), action1)
        print(calculate(float(total), float(var3), action2))

def main():
    amount=float(input("How many numbers? (2 or 3) "))
    if(amount==2):
        calc2()
    elif(amount==3):
        calc3()
    else:
        print("2 or 3 numbers!?")

main()