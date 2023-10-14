import words
from words import words

def filter_word_list(words, clues):
    filtered_words = []
    for word in words:
        word_upper = word.upper()
        secret = True
        for guess in clues:
            result = check_word(word_upper, guess[0])
            if result != guess[1]:
                secret = False
                break
        if secret:
            filtered_words.append(word)

    return filtered_words

def check_word(secret, guess):
    output = ["grey"] * 5
    secret_counts = {}
    guess_counts = {}
    for i in range(len(output)):
        if secret[i] == guess[i]:
            output[i] = "green"
        else:
            secret_counts[secret[i]] = secret_counts.get(secret[i], 0) + 1
            guess_counts[guess[i]] = guess_counts.get(guess[i], 0) + 1
    for i in range(len(output)):
        if output[i] != "green" and guess[i] in secret_counts and secret_counts[guess[i]] > 0:
            output[i] = "yellow"
            secret_counts[guess[i]] -= 1
    return output

def easy_game(secret):
    print(">" + secret)
    count = 0
    i = 0
    while i < 6:
        for word in words:
            if len(word) == len(secret) or len(word) <= 5:
                count += 1
                print(count + " words possible:\n")
                print (word)
        i += 1

    if check_word(secret, word) == ["green"] * 5:
            print("Answer:", secret)

if __name__ == "__main__":
    filter_word_list()
    check_word()
    easy_game()