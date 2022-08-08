
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

month = calendar.month_abbr[datetime.today().month]
year = datetime.now().strftime('%Y')

sign = "-"

password = month + sign + uppercaseLetter1 + lowercaseLetter1 + sign + number1 + number2 + sign + uppercaseLetter2 + lowercaseLetter2 + sign + year

print(password)