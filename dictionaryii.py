import json
from difflib import get_close_matches

data = json.load(open("data.json"))
word = input("Write the word that you want to know its meanning: ")

def translate (word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data :
        return data[word.title()]
    elif word.upper() in data :
        return data[word.upper()]
    elif len (get_close_matches(word , data.keys())) > 0 :
        print ("Do you mean this word %s" %get_close_matches(word , data.keys())[0])
        decide = input("if this is the word do you mean press y if no press n")
        if decide == "y" :
            return data [get_close_matches(word,data.keys())[0]]
        else :
            print ("-----------wrong word----------------")

    else :
        print ("---------------wrong word----------------")

output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print (output)
