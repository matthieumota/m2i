def say_hello(name: str = None) -> str:
    """
    Affiche Hello.
    """
    if name is None:
        name = 'World'

    print(f'Hello {name}')
    return f'Hello {name}'

result = say_hello('Fiorella') + ', ' + say_hello('John')
say_hello()
print(result.upper())

def addition(*numbers: int) -> int:
    return sum(numbers)

print(addition(1, 2) + addition(3, 4))
print(addition(1, 2, 3, 4, 5, 6, 7, 8, 9))

print(1, 2, 3, 4, 5, sep='-')
say_hello(name='Andri')
