#!/usr/bin/python3
# Aria Omidi
# CPS109 -- Assignment 2
# Translator English-Frisian and Frisian-English

# ========================================
# Step 1:
# Making the mother dictionary
# I wrote a domain generator program and used it to make my dictionary here
# Domains I covered in this dictionary are about:
# traffic jams and a little bit of school
# I also made another dictionary of EtoF using main dictionary called EtoFCaps

EtoF = {
    "i": "ik",
    "am": "bin",
    "you": "jo",
    "he": "hy",
    "she": "se",
    "no one": "nimmen",
    "The": "De",
    "the": "de",
    "so": "dat",
    "to": "nei",
    "and": "en",
    "a": "in",
    "was": "wie",
    "eat": "yt",
    "drink": "drinke",
    "overslept": "oersliep",
    "late": "let",
    "school": "skoalle",
    "bread": "brea",
    "good": "goede",
    "red": "reade",
    "wine": "wyn",
    "happy": "lokkich",
    "totally": "folslein",
    "completely": "hielendal",
    "person": "minske",
    "today": "hjoed",
    "nothing": "neat",
    "doing": "dwaan",
    "be": "wêze",
    "seems": "lykje",
    "Tom": "Tom",
    "commute": "pendelje",
    "everyday": "eltse-dei",
    "sustain": "folhâlde",
    "no": "Nee",
    "maximum": "maksimum",
    "capacity": "kapasiteit",
    "some": "guon",
    "roads": "wegen",
    "transport": "ferfier",
    "movement": "beweging",
    "in": "yn",
    "recent": "resint",
    "fix": "meitsje",
    "at": "by",
    "place": "plak",
    "hours": "oeren",
    "as": "as",
    "traffic": "ferkear",
    "plying": "pleagje",
    "reasons": "redenen",
    "during": "tidens",
    "anytime": "wannear-dan-ek",
    "problem": "probleem",
    "when": "wannear",
    "mostly": "meast",
    "hampered": "hindere",
    "years": "jierren",
    "is": "is",
    "has": "hat",
    "their": "harren",
    "number": "nûmer",
    "main": "foarnaamste",
    "vehicles": "weinen",
    "for": "foar",
    "commercial": "kommersjeel",
    "particular": "beskaat",
    "if": "as",
    "it": "it",
    "street": "strjitte",
    "affair": "affêre",
    "population": "befolking",
    "people": "folk",
    "aided": "holpen",
    "way": "wei",
    "period": "perioade",
    "personal": "persoanlik",
    "results": "resultaten",
    "home": "thús",
    "time": "tiid",
    "road": "wei",
    "cities": "stêden",
    "increase": "tanimme",
    "well": "goed",
    "result": "resultaat",
    "or": "of",
    "only": "allinnich",
    "of": "fan",
    "than": "as",
    "have": "hawwe",
    "peak": "peak",
    "public": "iepenbier",
    "surge": "surge",
    "but": "mar",
    "work": "wurk",
    "growing": "groeie",
    "development": "ûntwikkeling",
    "unprecedented": "ongekend",
    "use": "brûke",
    "an": "an",
    "certain": "beskaat",
    "congestion": "oerlêst",
    "increasing": "tanimmend",
    "big": "grut",
    "there": "dêr",
    "on": "op",
    "increased": "ferhege",
    "industrial": "yndustrieel",
    "made": "makke",
    "jams": "jam",
    "jam": "jam",
    "occurs": "optreedt",
    "by": "troch",
    "build": "bouwe",
    "back": "rêch",
    "over": "oer",
}

# I wrote another dictionary only for capitalized words for EtoF
EtoFCaps = {
    English.capitalize(): Frisian.capitalize() for English, Frisian in EtoF.items()
}
# ========================================
# Step 2:
# Making FtoE dictionary using EtoF by reverse function

# I actually didn't make a function for reversing dictionaries
# But I used dictionary comprehension because it is more efficiant

# As you can see I also commented reverseDictionary function down below

# def reverseDictionary(dictionary):
#     FtoE = {}

#     for english, frisian in dictionary.items():
#         FtoE[frisian] = english
#     return FtoE


FtoE = {frisian: english for english, frisian in EtoF.items()}

# I wrote another dictionary only for capitalized words for FtoE
FtoECaps = {
    frisian.capitalize(): english.capitalize() for frisian, english in FtoE.items()
}


# ========================================
# Step 3:
# A function to just translate from English to Frisian


def EnglishtoFrisian(English_string):
    UCletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LCletters = "abcdefghijklmnopqrstuvwxyz"
    letters = UCletters + LCletters
    charword = ""
    Frisian_string = ""
    for word in English_string.split():
        if word in EtoF:
            Frisian_string += EtoF[word] + " "

        elif word in EtoFCaps:
            Frisian_string += EtoFCaps[word] + " "

        elif word.endswith((".", "?", "!", ",")):
            for char in word:
                if char in letters:
                    charword += char

                else:
                    Frisian_string += EnglishtoFrisian(charword) + char
                    charword = ""
        else:
            Frisian_string += '"' + word + '"' + " "

    return Frisian_string


# ========================================
# Step 4:
# A function to just translate from Frisian to English


def FrisiantoEnglish(Frisian_string):
    UCletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LCletters = "abcdefghijklmnopqrstuvwxyz"
    letters = UCletters + LCletters
    charword = ""
    English_string = ""

    for word in Frisian_string.split():
        if word in FtoE:
            English_string += FtoE[word] + " "

        elif word in FtoECaps:
            English_string += FtoECaps[word] + " "

        elif word.endswith((".", "?", "!", ",")):
            for char in word:
                if char in letters:
                    charword += char

                else:
                    English_string += FrisiantoEnglish(charword) + char
                    charword = ""

        else:
            English_string += '"' + word + '"' + " "

    return English_string


# ========================================
# Step 5:
# Lists of sentences to translate
# I used pre recorded sentences instead of taking inputs from user

# You can uncomment this ESentences list and you will see the translation of them

# ESentences = [
#     "I drink good red wine and eat bread.",
#     "I overslept so I was late to school.",
#     "I am a completely happy person!",
#     "Tom seems to be doing nothing today.",
#     "Traffic jam or traffic congestion is an everyday affair in big cities"
# ]


ESentences = [
    "Traffic jam occurs when movement of vehicles is hampered at a particular place for some reasons over a certain period of time.",
    "If the number of vehicles plying on a street or road is increased than the maximum capacity it is build to sustain, it results in traffic jams.",
    "Traffic jam or traffic congestion is an everyday affair in big cities.",
    "It is the result of growing population and the increase in use of personal, public as well as commercial transport vehicle is an everyday affair in big cities.",
    "It is the result of growing population and the increase in use of personal, public as well as commercial transport vehicles.",
    "The congestion mostly occurs on the main roads during peak hours when people commute to work or on their way back home.",
    "But there is no fix time and an unprecedented surge in the number of vehicles on roads have made traffic jams anytime affair.",
    "The Industrial development in the recent years has only aided to the problem of traffic jam by increasing number of on road transport vehicles.",
]

FSentences = [
    "Ik drinke goede reade wyn en yt brea.",
    "Ik oersliep dat Ik wie let nei skoalle.",
    "Ik bin in folslein lokkich minske!",
    "Tom lykje nei wêze dwaan neat hjoed.",
    "Ferkear jam of ferkear oerlêst is an eltse-dei affêre yn grut stêden"
]

# ========================================
# Step 6:
# Test it out functions
# just a simple function to make my output.txt file beautiful
def outputEtoF():
    print("\n----------------English to Frisian translation----------------\n")
    for i in range(len(ESentences)):
        print("--------------------------------------")
        print("Input:", ESentences[i], "\n")
        print("Output:", EnglishtoFrisian(ESentences[i]))
        print("--------------------------------------")
    print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


def outputFtoE():
    print("\n----------------Frisian to English translation----------------\n")
    for i in range(len(FSentences)):
        print("--------------------------------------")
        print("Input:", FSentences[i], "\n")
        print("Output:", FrisiantoEnglish(FSentences[i]))
        print("--------------------------------------")
    print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print("Length of all dictionaries:", len(EtoF))
outputEtoF()
outputFtoE()
