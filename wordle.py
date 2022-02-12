language = str(input("Вы используете английскую версию wordle или русскую? Напишите EN для английской и RU для русской")) 


words = str(input("Enter letters: "))
word = list(words)
print(word)
numbers = (input("Enter pos-s: ").split())
print(numbers)

def removeElements(A, B):
    return ', '.join(map(str, A)) in ', '.join(map(str, B))

if language == 'RU':
    with open("sing.txt") as w:
        for line in w:
            shell = list(line)
            if removeElements(word, shell):
                print(''.join(shell))


