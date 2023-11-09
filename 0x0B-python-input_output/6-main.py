#!/usr/bin/python3
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_name = "my_list.json"
my_list = load_from_json_file(file_name)
print(my_list)
print(type(my_list))

file_name = "my_dict.json"
my_dict = load_from_json_file(file_name)
print(my_dict)
print(type(my_dict))

try:
    file_name = "my_set_doesnt_exist.json"
    my_set = load_from_json_file(file_name)
    print(my_set)
    print(type(my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    file_name = "my_fake.json"
    my_fake = load_from_json_file(file_name)
    print(my_fake)
    print(type(my_fake))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
