# DATE DETECTION
import re

text = "today is 27/12/2000, tomorow is 28/12/2000"

date_regex = re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')

fn = date_regex.findall(text)

# validate

for dt in fn:
    date = int(dt[0])
    month = int(dt[1])
    year = int(dt[2])


    
    if date <= 31 and month <= 12:
        print(f"Date: {date}\nMonth: {month}\nYear: {year}")
    else:
        print("Do you know:\nA year has 12 months and a month has 31, 30 or 28 days")

# STRONG PASSWORD DETECTION

import re

text = "" # your text here

pass_length_regex = re.compile(r'.{8,}')
pass_upper_regex = re.compile(r'[A-Z]')
pass_lower_regex = re.compile(r'[a-z]')
pass_digit_regex = re.compile(r'[0-9]')
pass_special = "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"

def check(text):
    if pass_length_regex.search(text) is None:
        return False
    if pass_upper_regex.search(text) is None:
        return False
    if pass_lower_regex.search(text) is None:
        return False
    if pass_digit_regex.search(text) is None:
        return False
    if " " in text:
        return False
    for i in pass_special:
        if i in text:
            return True
    return True
if check(text):
    print("Strong password")
else:
    print("weak password")

# strip() Method
# easy way to live lol 👨‍🦰👨‍🦰👨‍🦰

text = " fuck you bitch !! "
print(text.split())
