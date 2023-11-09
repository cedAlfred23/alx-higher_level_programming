#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

file_name = "my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, file_name)

file_name = "my_dict.json"
my_dict = {
    'id': 12,
    'name': "John",
    'places': ["San Francisco", "Tokyo"],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
save_to_json_file(my_dict, file_name)

try:
    file_name = "my_set.json"
    my_set = {132, 3}
    save_to_json_file(my_set, file_name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
