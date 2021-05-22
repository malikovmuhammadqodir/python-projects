import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(letter):
    letter = letter.lower()
    if letter in data:
        return data[letter]
    elif len(get_close_matches(letter,data.keys())) > 0:
        yesno = input("Did you mean %s instead? Enter y if yes or n if no: "% get_close_matches(letter,data.keys()))
        if yesno == 'y':
            return data[get_close_matches(letter,data.keys())[0]]  
        elif yesno == 'n':
            return 'this word does not macth please check it again'
        else:
            return 'we did not understand your input'
    else:
        return 'this word does not exists'     


input_word = input('enter your word>>')
output = translate(input_word)

if output == list:
    for item in output:
        print(item)
else:
    print(output)        

