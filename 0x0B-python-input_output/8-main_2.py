#!/usr/bin/python3
MyClass = __import__('8-my_class_2').MyClass
class_to_json = __import__('8-class_to_json').class_to_json

m = MyClass("John")
m.win()
print(type(m))
print(m)

p_mj = class_to_json(m)
print(type(p_mj))
print(p_mj)
