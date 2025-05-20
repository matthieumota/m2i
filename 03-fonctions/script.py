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
