"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jiri Putik
email: j.putik@gmail.com
discord: peen_cz
"""

# zadané texty

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


# databáze uživatelů, definice a konstanty

users = dict(
    bob = "123",
    ann = "pass123",
    mike = "password123",
    liz = "pass123"
)
page = 40 * "-"
result = dict()
result_length = dict()

# přihlášení uživatele a otestování

user_name = input("Please enter your name: ")
user_pass = input("Please enter your password: ")

if user_name not in users.keys() or users[user_name] != user_pass:
    print("unregistered user, terminating the program..")
    exit()
else:
    print(f"Welcome to the app, {user_name}")
print(page)
print("We have 3 texts to be analyzed.")
print(page)
text_nr = input("Enter a number btw. 1 and 3 to select: ")
if text_nr not in ("1", "2", "3"):
    print("bad number, exiting...")
    exit()
print(page)

# načtení a analýza textu

wrd_list_rough = TEXTS[(int(text_nr)-1)].split()
wrdlist = [word.strip(",.") for word in wrd_list_rough]   # očištění od znaků ".,"
result['words_nr'] = (len(wrdlist))
count_titleist = count_upper = count_lower = count_digit = sum_digit = 0    # nulování čítačů
for word in wrdlist:
    if not len(word) in result_length.keys():
        result_length[len(word)] = 1
    else:
        result_length[len(word)] += 1
    count_titleist += 1 if word.istitle() else 0
    count_upper += 1 if word.isupper() and word.isalpha() else 0
    count_lower += 1 if word.islower() and word.isalpha() else 0
    if word.isdigit():
        count_digit += 1
        sum_digit += int(word)

# zapsání výsledků

result['titleist'] = count_titleist
result['uppercase'] = count_upper
result['lowercase'] = count_lower
result['digit'] = count_digit
result['sum_digit'] = sum_digit

print(f"""There are {result['words_nr']} words in the selected text.
There are {result['titleist']} titlecase words.
There are {result['uppercase']} uppercase words.
There are {result['lowercase']} lowercase words.
There are {result['digit']} numeric strings.
The sum of all the numbers is {result['sum_digit']}.
{page}""")

# graf hlavička

max_length = 2 + max(list(result_length.values())) # zjištění potřebné šířky grafu, přičíst 2, aby to bylo hezký :-)  
print(f"LEN|{"OCCURENCES":^{max_length}}|NR.")
print(page)

# graf výpis hodnot

list_result_length = list(result_length.keys())
list_result_length.sort()
for index in (list_result_length):
    print(f"{index:>3}|{"*" * result_length[index]:<{max_length}}|{result_length[index]}")