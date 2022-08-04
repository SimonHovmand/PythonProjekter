

from itertools import combinations_with_replacement
from string import ascii_letters


word = "The lazy dog jumped over the quick brown fox"
print(" ")
print("Word input: %s" % (word))
message = ""
shift = 2


for char in word:
    i = ord(char)
    i += shift
    if i > ord("z"):
        i -= 26
    
    character = chr(i)
    message += character

    result = message.replace('"', " ")


print("Word output: %s" % (result))
print(" ")