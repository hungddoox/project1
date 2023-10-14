import words
from words import words

def check_word(secret, guess):
    output = ["grey"] * 5
    secret_list = {}
    guess_list = {}
    for i in range(len(output)):
        if secret[i] == guess[i]:
            output[i] = "green"
        else:
            secret_list[secret[i]] = secret_list.get(secret[i], 0) + 1
            guess_list[guess[i]] = guess_list.get(guess[i], 0) + 1
    for i in range(len(output)):
        if output[i] != "green" and guess[i] in secret_list and secret_list[guess[i]] > 0:
            output[i] = "yellow"
            secret_list[guess[i]] -= 1
    return output

def known_word(clues):
    known_word_list = ["_"] * 5
    for guess, clue in clues:
        for i in range(5):
            if clue[i] == "green":
                known_word_list[i] = guess[i]
    known_word = "".join(known_word_list)
    return known_word

def no_letters(clues):
    grey_letters = set()
    for letters, clue in clues:
        for i in range(len(letters)):
            letter = letters[i]
            if clue[i] == "grey" and letter not in letters[i+1:]:
                grey_letters.add(letter)
    no_letters = sorted(grey_letters)
    return ''.join(no_letters)

def yes_letters(clues):
    green_yellow_letters = set()
    for letters, clue in clues:
        for i in range(len(letters)):
            if clue[i] == "green" or clue[i] == "yellow":
                green_yellow_letters.add(letters[i])
    yes_letters = sorted(green_yellow_letters)
    return ''.join(yes_letters)

def game(secret):
    attempts = 0
    clues = []
    print(">> game(\"" + secret + "\")")
    while attempts < 6:
        print("Known:", known_word(clues))
        print("Green/Yellow Letters:", yes_letters(clues))
        print("Grey Letters:", no_letters(clues))
        print()

        for word in words:
            word = word.upper()
        if not words(word) or len(word) != 5:
            print("Not a word. Try again")
            print("> ")

        attempts += 1

        clues.append((word, check_word(secret, word)))
        print("Known:", known_word(clues))
        print("Green/Yellow Letters:", yes_letters(clues))
        print("Grey Letters:", no_letters(clues))
        print()

        if check_word(secret, word) == ["green"] * 5:
            print("Answer:", secret)
            break
        
    print(">>>")

if __name__ == "__main__":
    check_word()
    known_word()
    no_letters()
    yes_letters()
    game()
