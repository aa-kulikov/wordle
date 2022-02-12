import sys

def removeElements(A, B):
    return ', '.join(map(str, A)) in ', '.join(map(str, B))

def posElements(num, word, word_f):
    if len(num) == 1:
        if word_f[int(num[0])] == word[0]:
            print(''.join(word_f))
    if len(num) == 2:
        if word_f[int(num[0])] == word[0] and word_f[int(num[1])] == word[1]:
            print(''.join(word_f))
    if len(num) == 3:
        if word_f[int(num[0])] == word[0] and word_f[int(num[1])] == word[1] and word_f[int(num[2])] == word[2]:
            print(''.join(word_f))



language = str(input("Вы используете английскую версию wordle или русскую? Напишите EN для английской и RU для русской: ")) 

if language != 'RU' and language != 'EN':
    print('Wrong language. Start me again')
    sys.exit(0)

words = str(input("Enter letters: "))
word = list(words)
print(word)
numbers = (input("Enter pos-s, with spaces. Enter none if you don't know pos-s: ").split())
print(numbers)

bans = str(input("Enter banned characters: "))
ban = list(bans)
print(ban)

if len(numbers) != len(word) and len(numbers) > 0:
    print('Incorrect input. Start me again.')
    sys.exit(0)

print('Возможные варианты: ')
if language == 'RU':
    with open("words.txt") as w:
        for line in w:
            shell = list(line)
            if not any(item in shell for item in ban) and len(numbers) > 0: 
                posElements(numbers, word, shell)
            elif all(item in shell for item in word) and len(numbers) == 0 and not any(item in shell for item in ban) :
                print(''.join(shell))
if language == 'EN': 
    with open("words_en.txt") as w:
        for line in w:
            shell = list(line)
            if not any(item in shell for item in ban) and len(numbers) > 0: 
                posElements(numbers, word, shell)
            elif all(item in shell for item in word) and len(numbers) == 0 and not any(item in shell for item in ban) :
                print(''.join(shell))
