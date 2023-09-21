# FILEPATH: sort_strings_by_length.py

strings = ['a', 'as', 'aabaat', 'car', 'dove', 'python']
print(strings)
strings.sort(key=lambda x: len(x))
print(strings)
strings.sort(key=lambda x: len(x), reverse=True)
print(strings)
