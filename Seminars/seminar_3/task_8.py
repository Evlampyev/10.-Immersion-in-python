# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того,
# у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться на любое большее количество друзей.


friends_dict = {
    'Алекс': ('кружка', 'ложка', 'спички', 'топор'),
    'Павел': ('кружка', 'спички', 'топор'),
    'Илья' : ('кружка', 'рюмка', 'спички'),
}

all_things = set()
for friend in friends_dict:
    friend_things = set(friends_dict[friend])
    friends_dict[friend] = friend_things
    all_things = all_things | friend_things

print(f"{all_things = }")
print(f"{friends_dict = }")

all_friends_have = all_things  # Какие вещи взяли все три друга
friends_with_unique_things = dict()  # Какие вещи уникальны, есть только у одного друга
friends_not_have_things = dict()  # Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует

for friend in friends_dict:
    all_friends_have = all_friends_have & friends_dict[friend]
    temp_set = all_things.copy()
    not_have_set = all_things.copy()
    for another_friend in friends_dict:
        if another_friend != friend:
            temp_set -= friends_dict[another_friend]
            not_have_set = not_have_set & friends_dict[another_friend]
    if len(temp_set) > 0:
        friends_with_unique_things[friend] = temp_set
    if len(not_have_set) > 1:
        for thing in not_have_set:
            if thing not in friends_dict[friend]:
                if friend in friends_not_have_things:
                    friends_not_have_things[friend] += [thing]
                else:
                    friends_not_have_things[friend] = [thing]

print(f'{all_friends_have = }')
print(f'{friends_with_unique_things = }')
print(f'{friends_not_have_things = }')
