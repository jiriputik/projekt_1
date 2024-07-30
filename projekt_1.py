"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jiri Putik
email: j.putik@gmail.com
discord: peen_cz
"""

# zadané texty, texty číslo 4, 5 a 6 přidány z testovacích důvodů

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
garpike and stingray are also present.''',
'''Ezechiel 25, 17:
Cesta spravedlivého ze všech stran lemována jest 
nespravedlností, sobectvím a tyranií lidské zloby. 
Požehnán buď ten, kdo ve jménu lásky a dobré vůle 
vyvede slabé z údolí temnoty. Neb ten jest skutečným 
pastýřem a spasitelem zbloudilých dětí. 
A já srazím k zemi mocným trestem a divokým hněvem všechny, 
kdo se pokusí otrávit a zničit mé bratry. A když uvalím 
svou mstu na Tebe, seznáš, že jméno mé je Bůh.''',
'''Servít je vůl!''',
'''12.5 je 1/8 ze 100. Kolik je jedna osmina z 200, 300 a 400? Kolik je 7! ?'''
]


# databáze uživatelů, definice a konstanty

users = dict(
    bob = "123",
    ann = "pass123",
    mike = "password123",
    liz = "pass123"
)
page = 40 * "-"
result = dict()                     # proměnná pro evidenci výsledků
result_length = dict()              # proměnná pro data grafu
texts_count = len(TEXTS)

# přihlášení uživatele a otestování

user_name = input("Please enter your name: ")
user_pass = input("Please enter your password: ")

if user_name not in users.keys() or users[user_name] != user_pass:
    print("unregistered user, terminating the program..")
    exit()
else:
    print(f"Welcome to the app, {user_name}")
print(page)

# tady by IMHO bylo lepší dát while cyklus, který počká až na správný vstup, ale když to má po zadání špatného skončit, tak pojďme takto:

print(f"We have {texts_count} texts to be analyzed.")
print(page)
text_nr = input(f"Enter a number btw. 1 and {texts_count} to select: ")
if text_nr.isnumeric() and int(text_nr) in range(1, texts_count + 1):
    pass
else:
    print("bad number, exiting...")
    exit()
print(page)

# načtení a analýza textu

wrd_list_rough = TEXTS[(int(text_nr)-1)].split()
wrdlist = list()
numbers_list = list()
problematic_numbers = list()
is_float = False
is_unsure_number = False

for word in wrd_list_rough:                 # očištění od znaků, které nejsou alfanumerické a základní ošetření některých čísel
       
    word_clean = ''
    for letter in word:
        if letter.isalnum() or letter in ("/", "*", "-", "+", "!", "."):   
            if letter == "." and word_clean.isdigit():
                word_clean += (letter)
                is_float = True
            elif letter in ("/", "*", "-", "+", "!") and word_clean.isdigit():
                word_clean += (letter)
                is_unsure_number = True
            elif letter.isalpha():
                word_clean += (letter)
            elif letter.isdigit():
                word_clean += (letter)
    if not is_float and not is_unsure_number:
        wrdlist.append(word_clean)
    else:
        if is_unsure_number:
            problematic_numbers.append(word_clean)
            is_unsure_number = False
        else:
            is_float = False
            if word_clean[-1].isdigit():
                wrdlist.append((word_clean))
            else:
                wrdlist.append(word_clean.rstrip("."))

wrdlist = list(filter(None, wrdlist))                                 # odstranění nulových slov, které mohly vzniknout například při nekonzistentním formátování, například vložení mezery před interpunkci

result['words_nr'] = (len(wrdlist)) + len(problematic_numbers)  # celkový počet slov

count_titleist = count_upper = count_lower = count_digit = count_float_digit = sum_digit = 0    # nulování čítačů

# analýza slov na očištěném seznamu

for word in wrdlist:
    if not len(word) in result_length.keys():
        result_length[len(word)] = 1
    else:
        result_length[len(word)] += 1
    count_titleist += 1 if (word.istitle() and word[0].isalpha()) else 0
    count_upper += 1 if word.isupper() and word.isalpha() else 0
    count_lower += 1 if word.islower() and word.isalpha() else 0
    if word.isdigit() or word.find(".") != -1:
        if word.find(".") == -1:
            count_digit += 1
            sum_digit += int(word)
        else:
            count_float_digit += 1
            sum_digit += float(word)

# zapsání výsledků

result['titleist'] = count_titleist
result['uppercase'] = count_upper
result['lowercase'] = count_lower
result['digit'] = count_digit
result['float_digit'] = count_float_digit
result['sum_digit'] = sum_digit

print(f"""There are {result['words_nr']} words in the selected text.
There are {result['titleist']} titlecase words.
There are {result['uppercase']} uppercase words.
There are {result['lowercase']} lowercase words.
There are {result['digit']} integer numeric strings.
There are {result['float_digit']} float numeric strings.
The sum of all the numbers is {result['sum_digit']}.
{page}""")

# graf hlavička

max_length = 9 + max(list(result_length.values())) # zjištění potřebné šířky grafu, přičíst 9 (aby se tam vešlo i OCCURECES) a aby to bylo hezký a pod sebou :-)  
print(f"LEN|{"OCCURENCES":^{max_length}}|NR.")
print(page)

# graf výpis hodnot

list_result_length = list(result_length.keys())
list_result_length.sort()
for index in (list_result_length):
    print(f"{index:>3}|{"*" * result_length[index]:<{max_length}}|{result_length[index]}")

# výpis problematických čísel

print(page)
if len(problematic_numbers):
    print("I didn't know how to recogize this strings or numbers:", *problematic_numbers, sep="\n")