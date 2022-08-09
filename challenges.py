#Challenges 1

string = "The lazy dog jumped over the quick brown fox"
message = ""
shift = 2

for char in string:
    i = ord(char)
    i += shift
    if i > ord("z"):
        i -= 26
   
    character = chr(i)  
    message += character

    result = message.replace('"', " ")

print(" ")
print("String input: %s" % (string))
print("String output: %s" % (result))
print(" ")


#Challenges 2

number1 = "123"
number2 = "-123"

def reverseNum(n):
   n = str(n)
   if n[0] == '-':
      a = n[::-1]
      return f"{n[0]}{a[:-1]}"
   else:
      return n[::-1]

print("Number1 input:", number1)
print("Number1 output:", reverseNum(number1))
print("")
print("Number2 input:", number2)
print("Number2 output:", reverseNum(number2))
print("")
