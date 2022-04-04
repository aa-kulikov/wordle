import sys
import random

def generate_the_word(infile):
    random_line = random.choice(open(infile).read().split('\n'))
    return random_line

def words_cmpr(word, secret):
    true = 0
    for i in range(len(word)):
        if (word[i] == secret[i]):
            true += 1
    if true == 5:
        true = 1
    else: 
        true = 0
    return true

def letter_cmpr(word, secret):
    let_cmpr = ['0', '0', '0', '0', '0'] 
    for i in range(len(word)):
        for j in range(len(word)):
            if (word[j] == secret[j]):
                let_cmpr[j] = '1'
            if (i != j) & (word[i] == secret[j]):
                let_cmpr[i] = '2'
    return let_cmpr

def graphic(word, secret, count):
    i = 0
    for x in range(count):
        l = letter_cmpr(word[i], secret)
        print(word[i], "//", l[0], l[1], l[2], l[3], l[4])
        i += 1

print("W O R D L E")
menu = str(input("Do you wish to play a game? (y/n) \n"))
if (menu == "Yes") | (menu == "yes") | (menu == "y"):
    print("Ok.\nWe shall play a WORDLE\n")
    language = str(input("What language do you prefer? Options are: RU, EN\n"))
    secret = "XXXXX"
    if ((language == "RU") | (language == "ru") | (language == "r")):
        print("Your task is to guess a 5 letter word. Good luck.")
        secret_word = generate_the_word("words.txt")
        print(secret)
    elif ((language == "EN") | (language == "en") | (language == "e")):
        print("Your task is to guess a 5 letter word. Good luck.")
        secret_word = generate_the_word("words_en.txt")
     # secret_word = "civie"
    count = 6
    game = 0;
    i = 0
    array = ["XXXXX", "XXXXX", "XXXXX", "XXXXX", "XXXXX", "XXXXX"]
    graphic(array, secret_word, count)
    while ((i != count) | (game == 1)):
        guess = str(input("Enter your word: "))
        if len(guess) == 5:
            array[i] = guess
            graphic(array, secret_word, count)
            i += 1
            if (words_cmpr(guess, secret_word)) == 1:
                game = 1
                break
        else:
            print("You typed wrong word. Try again.\n")
    if (game != 1):
        print("\nYou lost. It's okay, though. Good luck next time. ")
        print("Word was =", secret_word)
    elif (game == 1):
        print("Wow. You won. Congrats.")
        print("Word was =", secret_word)
    else:
        print("You have typed something wrong. Restart me please.")
        sys.exit(0)

else:
    print("Sorry to see you go. Start me again to execute game.")
    sys.exit(0)