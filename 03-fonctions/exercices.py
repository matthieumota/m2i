# Exercice 1
def show_message() -> str:
    return 'Bienvenue en Python !'

print(show_message())

# Exercice 2
def good_bye(name: str) -> str:
    return f'Au revoir, {name} !'

print(good_bye('Fiorella'))

# Exercice 3
addition = lambda *numbers: sum(numbers)
print(addition(1, 2, 3, 4, 5, 6, 7, 8, 9))

# Exercice 4
is_even = lambda n: n % 2 == 0
def is_even(n):
    return n % 2 == 0
print(is_even(1))
print(is_even(2))

# Exercice 5
numbers = [10, 20, 30, 40]
numbers.append(50)
numbers.remove(20)

for n in numbers:
    print(n)

# Exercice 6
student = {
    'name': 'Fiorella',
    'age': 5,
    'average_note': 10
}

student['average_note'] = 12
student['classroom'] = '1A'

for key, value in student.items():
    print(f'{key}: {value}')

for key, value, third in [['A', 1, 'k'], ['B', 2, 'k'], ['C', 3, 'k']]:
    print(key, value, third)

student['notes'] = [15, 14, 18, 7, 13, 19]

import statistics
print(statistics.mean(student['notes']))
print(sum(student['notes']) / len(student['notes']))

# Exercice 7
def stats(numbers: list) -> dict:
    return {
        'min': min(numbers),
        'max': max(numbers),
        'mean': statistics.mean(numbers)
    }

print(stats([10, 20, 30, 40]))

# Exercice 8
import re
def word_frequency(sentence: str) -> dict:
    sentence = re.sub(r'[^a-zA-Z \'\-\n]', '', sentence)
    words = sentence.split()
    result = {}

    for word in words:        
        w = word
        result[w] = result.get(w, 0) + 1

    return result

print(word_frequency('bonjour, le monde, bonjour: aujourd\'hui. ca va ?'))

# Exercice 9
def merge_dicts(*dicts: dict) -> dict:
    result = {}

    for dict in dicts:
        for key, value in dict.items():
            defaultValue = 0
            current = result.get(key, defaultValue)
            if type(value) == str:
                defaultValue = ''
                value = str(value)
                current = str(result.get(key, defaultValue))
            result[key] = current + value

    return result

print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
print(merge_dicts({'a': 'a', 'b': 10}, {'b': 'b', 'c': 'c'}))

# Exercice 10
def sort_by_key(items: list[dict], field: str) -> list[dict]:
    return sorted(items, key=lambda item: item[field])

print(sort_by_key([{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}], 'age'))

# Exercice 11
def generate_matrix(size):
    result = []

    for line in range(size):
        new_line = []
        for column in range(size):
            new_line.append(line + column)

        result.append(new_line)

    return result

print(generate_matrix(5))
