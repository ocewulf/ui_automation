import json

# dict = {'name': 'xiaoA', 'age':12}
# json = json.dumps(dict)
# print(type(json))
# print(json)

# dict01 = {'name': 'xiaoB', 'age': 22, 'id': '430221098509152652'}
# with open('test.json', 'w', encoding='utf-8') as json_f:
#     json.dump(dict01, json_f)

# json_str = {'name': 'xiaoB', 'age': 22, 'id': '430221098509152652'}
# dict02 = json.loads(json_str)
# print(type(dict02))
# print(dict02)

with open('../data/test.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    print(data)
    print(type(data))