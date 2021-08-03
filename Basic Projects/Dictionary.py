"""
This is Basic Dictionary App using JSON file.
Feature:
1) Give result even when words given in different characters cases.
2) Give result if the input has spelling mistake and data has the nearby word.
"""

import json
from difflib import get_close_matches

#Loading JSON, path provided for JSON
data = json.load(open("Data Resource\Dictionarydata.json"))
print("|","Welcome To Dictionary App".center(70,"-"),"|")
#Function Starts
def translate(word):
    word = word.lower()
    #checking for word
    if word in data:
        return data[word]
    #When input given first letter capital else small
    elif word.title() in data:
        return data[word.title()]
    #When Input in upper case
    elif word.upper() in data:
        return data[word.upper()]
    #If there is close match to the given input
    elif len(get_close_matches(word , data.keys())) > 0 :
        print("did you mean %s instead" %get_close_matches(word, data.keys())[0],": ")
        decide = input("press Y for Yes or N for No: ")
        if decide == "y" or decide == "Y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n" or decide == "N":
            return("Word not found in Dictionary")
        else:
            #If something else input other then Y or N
            return("You have entered wrong input please enter just Y or N")
    #If word not found
    else:
        return("Word not found in Dictionary")
    data.close()


#Main Section
word = input("Enter the word you want to search: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print("->",item)
else:
    print(output)