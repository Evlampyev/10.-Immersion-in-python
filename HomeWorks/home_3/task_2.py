# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.
# Отсортируйте по убыванию значения количества повторяющихся слов.
from itertools import islice
import operator

text = "The quick brown fox jumps over the lazy dog. Lazy dog, lazy fox!"
LIMIT = 10
dict_words = {}
words = []
word = ''
for ch in text:
    if ch.isalpha():
        word += ch
    else:
        words.append(word.lower())
        word = ''
words = ' '.join(words).split()
# print(*words)

for word in words:
    dict_words[word] = dict_words.get(word, 0) + 1

count = 0
sort_dict_words = sorted(dict_words.items(), key=operator.itemgetter(1), reverse=True)
result = []
# print(sort_dict_words)
for word in sort_dict_words:
    if count < LIMIT:
        result.append(word)
        count += 1
    else:
        break
print(result)
