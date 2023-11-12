import json

with open('user.json', 'r', encoding='utf-8') as f:
    json_file = json.load(f) # загрузка JSON из файла и сохранение в dict или list

print(f'{type(json_file) = }\n{json_file = }')
print(f'{json_file["name"] = }')
print(f'{json_file["address"]["geo"] = }')
print(f'{json_file["email"] = }')


# json_list = json.loads(json_text)
# загрузка JSON из строки и сохранение в dict или list