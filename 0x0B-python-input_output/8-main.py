#!/usr/bin/python3
MyClass = __import__('8-my_class').MyClass
class_to_json = __import__('8-class_to_json').class_to_json

p_m = MyClass("John")
p_m.number = 89
print(type(p_m))
print(p_m)

mj = class_to_json(p_m)
print(type(mj))
print(mj)
