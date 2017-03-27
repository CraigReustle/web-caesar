def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"     #string of all letters
    for index in range(len(alphabet)):          #loop 0 to 25
        if alphabet[index] == letter.lower():   #if lowecase letter matches the letter of alphabet at current index
            return index                        #return index


def rotate_character(char, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if char.isalpha() == True:
        newpos = alphabet_position(char) + rot
        if newpos > 25:
            newpos = newpos % 26
        if char in alphabet:
            return alphabet[newpos]
        else:
            return alphabet[newpos].upper()
    else:
        return char

def encrypt(text,rot):
    newmess = ""
    for letter in text:
        newmess = newmess + rotate_character(letter,rot)
    return newmess
