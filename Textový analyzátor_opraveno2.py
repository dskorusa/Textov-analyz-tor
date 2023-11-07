# TODO hlavička
'''
"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: David Skoruša
email: d.skorusa@post.cz
discord: David Skoruša#7746
"""
import
'''
# TODO texty určené k analýze
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
# TODO registrovaní uživatelé
users = {"bob": "123", 
        "ann": "pass123", 
        "mike": "password123", 
        "liz": "pass123"
}
# TODO výpis registrovaných uživatelů
print("+------+-------------+")
print("| user |   password  |")
print("+------+-------------+")
for user, password in users.items():
    print(f"| {user:<4} | {password:<12}|")
print("+------+-------------+")

# TODO vstup uživatele (přihlášení a analýza)
(print("Vítám tě v programu na analýzu textu"))
username = input("Zadej user:")
password = input("Zadej password:")
print("----------------------------------------")

if username in users and users[username] == password: 
    print("-" * 40)
    print(f"Welcome to the app,{username}")
    print(f"We have {len(TEXTS)} texts to be analyzed.")

    select = input("Enter a number btw. 1 and 3 to select:")
    if select.isdigit() and 1 <= int(select) <= len(TEXTS):
        choice_text = TEXTS[int(select) - 1]
    
        words = choice_text.split()
        titlecase_words = sum(1 for word in words if word.istitle())
        uppercase_words = sum(1 for word in words if all(letter.isupper() for letter in word) and 1 for word in words if all(letter.isalpha() for letter in word))
        lowercase_words = sum(1 for word in words if word.islower())
        numeric_strings = sum(1 for word in words if word.isnumeric())
        sum_of_numbers = sum(int(word) for word in words if word.isnumeric())

        word_lengths = [len(word.strip(".,?!")) for word in words]
        word_length_counts = {}
        for length in word_lengths:
            word_length_counts[length] = word_length_counts.get(length, 0) + 1

        print("-" * 40)
        print(f"There are {len(words)} words in the selected text.")
        print(f"There are {titlecase_words} titlecase words.")
        print(f"There are {uppercase_words} uppercase words.")
        print(f"There are {lowercase_words} lowercase words.")
        print(f"There are {numeric_strings} numeric strings.")
        print(f"The sum of all the numbers {sum_of_numbers}")
        print("-" * 40)
        print("LEN| OCCURENCES |NR.")
        print("-" * 40)
        for length, count in sorted(word_length_counts.items()):
            print(f"{length:3}| {'*' * count:12}| {count}")
    else: 
        print("Invalid input. Program will terminate.")
else: 
    print("Unregistered user, terminanting the program.")
