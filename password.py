
import random
from time import strftime

import calendar
from datetime import datetime

uppercaseLetter1=chr(random.randint(65,90))
uppercaseLetter2=chr(random.randint(65,90))

lowercaseLetter1=chr(random.randint(97,122))
lowercaseLetter2=chr(random.randint(97,122))

number1=chr(random.randint(48,57))
number2=chr(random.randint(48,57))

specialsign=chr(random.randint(33,47))

month = calendar.month_abbr[datetime.today().month]
year = datetime.now().strftime('%Y')

password = month + "." + uppercaseLetter1 + uppercaseLetter2 + "." + number1 + specialsign + number2 + "." + lowercaseLetter1 + lowercaseLetter2 + "." + year

print(password)