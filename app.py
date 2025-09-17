import random
import os

print(f"Текущая папка: {os.getcwd()}")
print("Файлы в папке")
for file in os.listdir('.'):
    if file.endswith('.txt'):
        print(f"  - {file}")
file_name = input('Введите имя файла')
try:
    with open(file_name, 'r', encoding='utf-8') as file:
        Text = file.read()
    print(f"Файл '{file_name}' импортирован")

except FileNotFoundError:
    print(f"Файл '{file_name}' не найден")
    exit()
words = Text.split()
chain = {}
for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    if current_word not in chain:
        chain[current_word] = []
    chain[current_word].append(next_word)
word_upper = []
for i in range(len(words)):
    if words[i][0].isupper():
        word_upper.append(words[i])
start_word = random.choice(word_upper)
length = int(input('Введите количество слов в тексте: '))
result = [start_word]
current_word = start_word
for i in range(length - 1):
    if current_word in chain and chain[current_word]:
        next_word = random.choice(chain[current_word])
        result.append(next_word)
        current_word = next_word
    else:
        print("Цепь оборвалась на этом слове", current_word)
        break
print(' '.join(result))
