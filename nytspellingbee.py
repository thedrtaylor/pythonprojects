import os

def split(input):
    return [char for char in input]

def intro():
    print("")
    print("* "*20)
    print("This software finds all the possible words you can spell")
    print("using a set of letters provided by the user.")
    print("This is based off the NYT Spelling Bee puzzle.")
    print("IMPORTANT: For this program to run, it needs a dictionary.")
    print("Please make sure there is a file titled 'lexicon.txt'")
    print("in the same folder as this 'nytspellingbee.py' file.")
    print("* "*20)
    print("")

def getalphabet():
    print("What are today's available letters?")
    word = (input("all one word, no spaces: "))
    alphabet = sorted(list(set(split(word.lower()))))
    return alphabet

def gettestalphabet():
    alphabet = sorted(list(set(split(lower(input("adflmpu"))))))
    return alphabet

def getcenterletter():
    print("")
    print("The NYT Spelling Bee puzzle has one letter that is essential")
    print("to every word. What is that letter?")
    print("(Type 'no' if not using this rule.)")

    x = input("center letter: ")
    x = x.lower()
    if x == "no":
        return False, x
    else:
        return True, x

def gettestcenterletter():
    return True,"a"

def printuserinput(alphabet,using_center,center):
    print("")
    print("The letters you provided are:")
    print(alphabet)
    print("")
    if using_center:
        print("The essential letter is:" , center)
    else:
        print("You have chosen to not use the center letter.")

def gettestdictionary():
    dictionary = ["mudflap","alfalfa","alum","aluminum","damp","damn","plum"]
    return dictionary

def getdictionary():
    inputfilename = "lexicon.txt"
    dictionary = []
    with open(inputfilename, "r") as f:
        for line in f:
            dictionary.append(line.strip())
    return dictionary

def checkword(word,alphabet,using_center,center):
    x = split(word)
    for num in range(len(x)):
        if x[num] not in alphabet:
            return False, word
    if using_center:
        if center in x:
            return True, word
        else:
            return False, word
    else:
        return True, word

def addword(word,answers):
    answers.append(word)
    return answers

def removeshortwords(answers):
    truncatedanswers = []
    for num in range(len(answers)):
        word = answers[num]
        if len(answers[num]) >= 4:
            truncatedanswers.append(word)
    return truncatedanswers
# --------------------------------

intro()
alphabet = getalphabet()
using_center, center = getcenterletter()
dictionary = getdictionary()

answers = []
for x in range(len(dictionary)):
    wordisvalid,word = checkword(dictionary[x],alphabet,using_center,center)
    if wordisvalid:
        answers = addword(word,answers)

dictionary = getdictionary()

truncatedanswers = removeshortwords(answers)

print("* "*20)
print("")
print("all valid answers:")
for n in range(len(truncatedanswers)):
    print(truncatedanswers[n])
