consonants = "pkhlmnw' "
vowels = {"a":"ah", "e":"eh", "i":"ee", "o":"oh", "u":"oo"}
doubleVowels = {"ai":"eye", "ae":"eye", "ao":"ow", "au":"ow", "ei":"ay", "eu":"eh-oo",
                "iu":"ew", "oi":"oyo", "ou":"ow", "ui":"ooey"}

#w sound as v and w

def validate(text):
    text = text.lower()
    valid = True
    for letter in text:
        if letter not in consonants and letter not in vowels:
            print(letter.upper(), "is not a valid Hawaiian Character.")
            valid = False
    return valid

def pronounce(text):
    output = ""
    index = 0
    text = text.lower()

    while index < len(text):
        if index + 1 < len(text) and text[index:index+2] in doubleVowels:
            output += doubleVowels[text[index:index+2]]
            index += 2
        elif text[index] in vowels:
            output += vowels[text[index]] + "-"
            index += 1
        elif text[index] == ' ':
            if output[-1] == '-':
                output = output[:-1]
            output += text[index]
            index += 1
        elif text[index] in consonants:
            output += text[index]
            index += 1
        else:
            index += 1

        #handle double vowels using slide index += 2
        #otherwise check if vowel index += 1
        #otherwise it's "consonant" index += 1
    if output[-1] == "-":
        output = output[:-1]
    return output

def main():

    while True:
        text = input("Enter Hawaiian word to pronounce: ")
        text = text.lower()

        if validate(text):
            print(text, "is pronounced", pronounce(text))

            another = ''
            stop = False

            while True:
                another = input("Do you want to enter another word? Y/YES/N/NO ==> ")
                if another.lower() == "y" or another.lower() == "yes":
                    print()
                    break
                if another.lower() == "n" or another.lower() == "no":
                    stop = True
                    break
            
            if stop == True:
                break
        else:
            print()

main()