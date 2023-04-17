def pangram(input):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if letter not in input.lower():
            return False
    return True

input = "The quick brown fox jumps over the lazy dog"
print (pangram(input))
#