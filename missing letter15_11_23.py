#Find the missing letter
#Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.
#You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
#The array will always contain letters in only one case.

#Example:
#['a','b','c','d','f'] -> 'e'
#['O','Q','R','S'] -> 'P'

def find_missing_letter(chars):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    length_chars= len(chars)
    print(length_chars)

    
    for i in alphabet:
        if i == chars[0]:
            start= alphabet.index(i)
    print(start)

    new_alphabet= alphabet[start:length_chars+1]
    print(new_alphabet)
    print(chars)

    for letters in chars:
        if letters not in new_alphabet:
            return letters

print(find_missing_letter(['a','b','c','d','f']))
