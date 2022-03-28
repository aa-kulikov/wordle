import sys
import random


def generate_the_word(infile):
    random_line = random.choice(open(infile).read().split('\n'))
    return random_line

def graphic(word, count):
    for x in range(count):
        print("XXXXX")

print("W O R D L E")
menu = str(input("Do you wish to play a game? (y/n) \n"))
if (menu == "Yes") | (menu == "yes") | (menu == "y"):
    print("Ok.\nWe shall play a WORDLE\n")
    language = str(input("What language do you prefer? Options are: RU, EN\n"))
    secret = "XXXXX"
    if language == "RU":
        print("Your task is to guess a 5 letter word. Good luck.")
        secret_word = generate_the_word("words.txt")
        print(secret)
    elif language == "EN":
        print("Your task is to guess a 5 letter word. Good luck.")
        secret_word = generate_the_word("words_en.txt")
        count = 6
        game = 0;
        while ((count != 0) | (game == 1)):
            graphic(secret, count)
            guess = str(input("Enter your word:\n"))
            while len(guess) != 5:
                print("Wrong type, my friend. Try again.\n")
                guess = str(input("Enter your word:\n"))
            count -= 1
    else:
        print("You have typed something wrong. Restart me please.")
        sys.exit(0)

else:
    print("Sorry to see you go. Start me again to execute game.")
    sys.exit(0)